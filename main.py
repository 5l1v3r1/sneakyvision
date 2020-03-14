import platform
import webcam_capture as web_cap
import cv2
import terminate as trm
import keyboard
#import picam_capture as pi_cap

def main():

    if(platform.system() == "Linux"):
        picamState = input("Are you using a Pi Camera? y/n")

        if(picamState == "y"):
            print("Configuring as Pi Camera...")
            
        elif(picamState == "n"):
            print("Configuring as USB/IP Camera...")
            web_cap.WebcamCapture().start(300,300)
        else:
            print("Please type y or n")
    else:
        print("Configuring as USB/IP Camera...")
        web_cap.WebcamCapture().start(300,300)
    
    while True:
        if keyboard.read_key() == "q":
            print("hello")
            print(trm.Terminate.status)
            trm.Terminate.status = True

        if trm.Terminate.status == True:
            web_cap.WebcamCapture().stop()

if __name__ == "__main__":
    main()
