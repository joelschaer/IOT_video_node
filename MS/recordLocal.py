#!/usr/bin/env python3

import socket
import time
import picamera
import threading
import requests
from values import Configuration

class Record(threading.Thread):
    def __init__(self, t_before, t_after):
        #threading.Thread.__init__(self)
        super(Record, self).__init__()
        self._t_before = t_before
        self._t_after = t_after
        self._nameVideo = None
        self._storeVideo = False
        self._running = False
        
    def _get_backend_address(self):
        config = Configuration()
        config.load()
        return config.get('backend', 'address')
        
    def run(self):
        print("before "+ str(self._t_before))
        print("after "+ str(self._t_after))
        print("ip backend "+ self._get_backend_address())

        self._storeVideo = False
        self._running = True
        print("start")
        try:
            camera = picamera.PiCamera()
            camera.resolution = (640, 480)
            camera.rotation = 180
            camera.framerate = 24
            # for the circular buffer local recording
            stream = picamera.PiCameraCircularIO(camera, seconds=self._t_before)
            # recording buffer circular continuousl
            camera.start_recording(stream, format='h264')

            while True:
                camera.wait_recording(1)
                if self._storeVideo:
                    # Keep recording for 10 seconds and only then write the
                    # stream to disk
                    print("wait")
                    camera.wait_recording(self._t_after)
                    stream.copy_to(self._nameVideo + '.h264')
                    files = {'file': open(self._nameVideo + '.h264', 'rb')}
                    requests.post("http://" + self._get_backend_address() + ":3030/videos", files=files)
    
                    self._storeVideo = False
                    
                if self._running == False:
                    camera.stop_recording()
                    return
        except Exception as e:
            print(str(e))
            
    def stop(self):
        print("Stop")
        self._running = False
        
    def storeVideo(self, name = 'buubu'):
        print("store")
        self._nameVideo = name
        self._storeVideo = True
