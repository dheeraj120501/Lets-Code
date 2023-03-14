#pylint:disable=no-member
import cv2 as cv

# Blurring is used to smooth the image by removing noice from the image

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# kernel window size (ksize) ask for rows and columns and the blurring algo work on that kernal window through the whole image

# Averaging blur
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)