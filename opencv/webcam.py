from turtle import color
import cv2 as cv
camera=cv.VideoCapture(0)
while (True):
    ret, capture=camera.read()
    color=cv.cvtColor(capture, cv.COLOR_BGR2GRAY)
    cv.imshow("webcam", color)
    
    if cv.waitKey(1)==ord("q"):break
    
camera.release()
cv.destroyAllWindows()