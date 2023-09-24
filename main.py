import cv2 #OpenCV
from cv2 import VideoCapture, imshow #VideoCapture

canFeed = VideoCapture(0) #Webcam

def main():
    while True:
        ret, frame = canFeed.read()
        if not ret:
            print("Failed to capture frame")
            break
        imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    print("Press Q to quit")


main()