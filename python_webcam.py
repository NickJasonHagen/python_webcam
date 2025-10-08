import cv2
import numpy as np
import argparse
import time


# get the arguments from the cli
parser = argparse.ArgumentParser(description='Send a message to a Discord webhook')
parser.add_argument('-o', required=True, help='Outputfile')
parser.add_argument('-m', required=True, help='Cameramode image/video')
args = parser.parse_args()

if args.m == "image" or args.m == "jpg":
    cam = cv2.VideoCapture(0)
    # Capture one frame
    ret, frame = cam.read()

    if ret:
        cv2.imshow("Captured", frame)         
        cv2.imwrite(args.o, frame)          
        cv2.destroyWindow("Captured")       
    else:
        print("Failed to capture image.")

    cam.release() 
if args.m == "video" or args.m == "mp4":
    # Open the default camera
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(args.o, fourcc, 20.0, (frame_width, frame_height))
    #render to videofile for a duration
    start = time.time()
    while True:
        end = time.time()
        ret, frame = cam.read()
        out.write(frame)
        if (end - start) >= 10.0:
            break

    # Release the capture and writer objects
    cam.release()
    out.release()
    cv2.destroyAllWindows()
