#!/usr/bin/python3
# -*- coding: utf-8 -*-

from picamera import PiCamera, Color
from time import sleep
import datetime

PATH = '/home/pi/Documents/'

class Camera:
  def __init__(self):
    self.camera = PiCamera()
    self.camera.resolution = (1920,1080)
    self.camera.framerate = 15
    self.camera.annotate_background = Color('black')
    self.camera.annotate_text = str(datetime.datetime.now())
    self.camera.rotation = 180

  def start(self, name):
    self.camera.start_preview()
    self.camera.start_recording('%s.h264' %name)

  def stop(self):
    self.camera.stop_recording()
    self.camera.stop_preview()

camera = Camera()
camera.start("yann")
time.sleep(10)
camera.stop()

