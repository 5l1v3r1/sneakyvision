import platform
from webcam_capture import WebcamCapture
from webcam_show import WebcamShow
#from picam_capture import PicamCapture
import cv2
import terminate as trm
#import picam_capture as pi_cap

def webcamThread(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Dedicated thread for showing video frames with VideoShow object.
    Main thread serves only to pass frames between VideoGet and
    VideoShow objects/threads.
    """

    video_getter = WebcamCapture(source).start()
    video_shower = WebcamShow(video_getter.frame).start()
    

    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

        frame = video_getter.frame
        
        video_shower.frame = frame

def main():
    
    if(platform.system() == "Linux"):
    
        picamState = input("Are you using a Pi Camera? y/n")

        if(picamState == "y"):
            print("Configuring as Pi Camera...")
            
        elif(picamState == "n"):
            print("Configuring as USB/IP Camera...")
            webcamThread()
        else:
            print("Please type y or n")
    else:
        print("Configuring as USB/IP Camera...")
        webcamThread()
        
        
if __name__ == "__main__":
    main()
