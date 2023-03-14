import cv2 as cv
import numpy as np
canvas = np.zeros((300, 300, 3), np.uint8)
k = 0
for i in range(0,300,20):
    l = k
    for j in range(0,300,20):
        if(l%2 == 0):
            cv.rectangle(canvas, (i,j), (i+20,j+20), (0,0,0), -1)
        else:
            cv.rectangle(canvas, (i,j), (i+20,j+20), (0,0,255), -1)
        l += 1
    k += 1
cv.circle(canvas, (150,150), 60, (0, 255, 0), -1)
cv.imshow("Result", canvas)
cv.waitKey(0)