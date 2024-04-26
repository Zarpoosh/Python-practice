# import numpy as np
import cv2 as cv

img1 = cv.imread('/home/minicode/Documents/project/python/opencv')
img2 = cv.imread('/home/minicode/Documents/project/python/opencv')
#added = img1 + img2


#added = cv.add(img1, img2)
added = cv.addWeighted(img1, 0.2, img2, 0.8, 0)

# img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# ret, maskimg = cv.threshold(img2gray, 40 ,255, cv.THRESH_BINARY)
# mask_inv = cv.bitwise_not(mask)  # noqa: F821

# img1_m = cv.bitwise_and(img1, img1, mask=maskimg)

cv.imshow('image1', img1)
cv.imshow('image2', img2)
cv.imshow('Added', added)

# cv.imshow('Mask', maskimg)
# cv.imshow('img1_m', img1_m)
# cv.waitKey(0)
# cv.destroyAllWindows()