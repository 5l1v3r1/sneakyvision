import cv2
from threading import Thread
from webcam_capture import WebcamCapture

class Trackbar:

    def nothing(x):
        pass

    def createTrackbars(self):
        self.fps='FPS'
        self.width='Width'
        self.height='Height'
        self.brightness='Brightness'
        self.contrast='Contrast'
        self.saturation='Saturation'
        self.exposure='Exposure'
        self.wnd = 'Camera Settings'
        # Begin Creating trackbars for each HSV value
        cv2.createTrackbar(self.fps, self.wnd, 0,   255, nothing)
        cv2.createTrackbar(self.width, self.wnd, 0,  255, nothing)
        cv2.createTrackbar(self.height, self.wnd, 0,  255, nothing)
        cv2.createTrackbar(self.brightness, self.wnd, 0,  255, nothing)
        cv2.createTrackbar(self.contrast, self.wnd, 0,   255, nothing)
        cv2.createTrackbar(self.saturation, self.wnd, 0,  255, nothing)

    def setCameraProperties(source=0):
        while not self.stopped():
            WebcamCapture().start().fps = cv2.getTrackbarPos(self.fps,self.wnd)
            WebcamCapture().start().width = cv2.getTrackbarPos(self.width,self.wnd)
            WebcamCapture().start().height = cv2.getTrackbarPos(self.height,self.wnd)
            WebcamCapture().start().brightness = cv2.getTrackbarPos(self.brightness,self.wnd)
            WebcamCapture().start().contrast = cv2.getTrackbarPos(self.contrast,self.wnd)
            WebcamCapture().start().saturation = cv2.getTrackbarPos(self.saturation,self.wnd)
            WebcamCapture().start().exposure = cv2.getTrackbarPos(self.exposure,self.wnd)
       

    def start(self):
        Thread(target=self.createTrackbars, args=()).start()
        Thread(target=self.setCameraProperties, args=()).start()
        return self

    def stop(self):
        self.stopped = True

