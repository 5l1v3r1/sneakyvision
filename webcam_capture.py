import cv2
import numpy as np
from imutils.video import FPS, WebcamVideoStream 
import imutils
import time
import sys
import terminate as trm

class WebcamCapture:
    def __init__(self):
        self.stream = WebcamVideoStream(src=0).start()
        self.fps = FPS().start()
        
    def start(self, width=None, height=None):
        while True:
            
            frame = self.stream.read()
            frame = imutils.resize(frame,width,height)    
            cv2.imshow("Frame", frame)
            self.fps.update()
            keyPressed = cv2.waitKey(1)
            
    def stop(self):
            self.fps.stop()
            print("[INFO] elasped time: {:.2f}".format(self.fps.elapsed()))
            print("[INFO] approx. FPS: {:.2f}".format(self.fps.fps()))
            self.sys.exit()
            
    