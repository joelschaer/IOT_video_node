import socket
import time
import picamera
import threading

class Stream(threading.Thread):

    def __init__(self):
        super(Stream, self).__init__()
        self._running = False

    def run(self):
        self._running = True
        print("start")
        try:
            with picamera.PiCamera() as camera:
                camera.resolution = (320, 240)
                camera.rotation = 180
                camera.framerate = 38

                server_socket = socket.socket()
                server_socket.bind(('0.0.0.0', 8034))
                server_socket.listen(0)
                connection = server_socket.accept()[0].makefile('wb')
                
                time.sleep(2)
                # Start recording, sending the output to the connection for 60
                # seconds, then stop
                camera.start_recording(connection, format='h264')
                while(True):
                    print("streammmm")
                    time.sleep(5)
                    #stopStream = True
                    
                    if self._running == False:
                        camera.stop_recording()
                        return
        except e:
            print(e)
        finally:
            connection.close()
            server_socket.close()
            
    def stop(self):
        print("Stop")
        self._running = False
