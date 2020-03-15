import cv2
import numpy as np
from threading import Thread

"""
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """


class WebcamCapture:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src=0):
        self.fps = 60
        self.width = 320
        self.height = 240
        self.brightness = 0
        self.contrast = 0
        self.saturation = 0
        # add gain here too
        self.exposure = 0


        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FPS, self.fps)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.stream.set(cv2.CAP_PROP_BRIGHTNESS, self.brightness)
        self.stream.set(cv2.CAP_PROP_CONTRAST, self.contrast)
        self.stream.set(cv2.CAP_PROP_SATURATION, self.saturation)
        # TODO: Add gain if its ps3eye
        self.stream.set(cv2.CAP_PROP_EXPOSURE, self.exposure)


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
                print("FPS : ", self.stream.get(cv2.CAP_PROP_FPS))
                print("BRIGHTNESS : ", self.stream.get(cv2.CAP_PROP_BRIGHTNESS))
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True

