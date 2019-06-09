#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import sleep
#from streamLocal import Stream
from recordLocal import Record

if __name__ == "__main__":
    t1 = Record()
    t1.start()
    print("starting")
    sleep(30)
    t1.storeVideo('blabla')
    print("stopping")
    t1.stop()
    t1.join()