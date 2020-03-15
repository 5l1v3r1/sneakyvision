
# TODO: work on this later
"""
import cv2
import numpy as np
from imutils.video import FPS
from picamera import PiCamera
import imutils
import time

class PicamCapture:
    def __init__(self):
        
        self.stream = pi.PiVideoStream().start()
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        
    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True
      """      
    