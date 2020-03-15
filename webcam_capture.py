import cv2
import numpy as np
from imutils.video import FPS, WebcamVideoStream 
import imutils
import time
import sys
import terminate as trm
from threading import Thread

"""
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

class WebcamCapture():   
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_BRIGHTNESS, 10)
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
          



   
   

 
        
        

    

   
    