#pylint:disable=no-member

import cv2 as cv
import numpy as np

# Splitting and merging an image into their respective color channels(BGR)

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)


# Working with a blank canvas with all black
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank,blank])
cv.imshow('Blue', blue)

green = cv.merge([blank,g,blank])
cv.imshow('Green', green)

red = cv.merge([blank,blank,r])
cv.imshow('Red', red)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)