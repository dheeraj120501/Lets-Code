#pylint:disable=no-member
import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats 2.jpg')
cv.imshow('Cats', img)

# For masking the blank should be of same size
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle_mask = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img,img,mask=circle_mask)
cv.imshow('Weird Shaped Masked Image', masked)

rectangle_mask = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
masked = cv.bitwise_and(img,img,mask=rectangle_mask)
cv.imshow('Weird Shaped Masked Image', masked)

new_shape = cv.bitwise_and(circle_mask, rectangle_mask)
cv.imshow('Weird Shape', new_shape)
masked = cv.bitwise_and(img,img,mask=new_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)
