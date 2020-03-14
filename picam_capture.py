import cv2
import numpy as np
from imutils.video import FPS
import sneaky_lib.pivideostream as pi
import imutils
import time

class PicamCapture:
    def __init__(self):
        
        self.stream = pi.PiVideoStream().start()
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
            
    