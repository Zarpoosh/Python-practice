import cv2 as cv
import numpy as np
import mediapipe 
from cvzone.HandTrackingModule import HandDetector

camera = cv.VideoCapture(0)
detector = HandDetector(detectionCon = 0.5, maxHands=4)

while(True):
    rec, frame = camera.read()
    hand, frame = detector.findHands(frame)
    if hand:
        hand1 = hand[0]
        lmlist1 = hand1["lmList"]
        print(lmlist1)

        length, info, frame = detector.findDistance(lmlist1[4][:-1], lmlist1[8][:-1], frame)
        print(f"length:===> {str(length)}")
         
    cv.imshow('webcam', frame)
    # keyexit = cv.waitKey(5) & 0xFF
    # if keyexit == 27:
        # break
    if cv.waitKey(1)==ord("q"):break

cv.destroyAllWindows()
camera.release()