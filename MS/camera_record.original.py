from picamera import PiCamera, Color
from time import sleep
import datetime

camera = PiCamera()
camera.resolution = (1920,1080)
camera.framerate = 15
camera.annotate_background = Color('black')
camera.annotate_text = str(datetime.datetime.now())
camera.rotation = 180
camera.start_preview()
camera.start_recording('/home/pi/Documents/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
