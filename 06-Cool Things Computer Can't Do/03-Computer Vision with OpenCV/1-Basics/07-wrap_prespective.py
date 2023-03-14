import cv2
import numpy as np

# Wrapping the prespective has an example in document scanners, where they make the image flat.
 
img = cv2.imread("../Resources/Photos/cards.jpg")
 
width,height = 250,350
pts1 = np.float32(([111,219],[287,188],[154,482],[352,440]))
pts2 = np.float32(([0, 0],[width, 0],[0, height],[width, height]))

# Transformation matrix
matrix = cv2.getPerspectiveTransform(pts1,pts2)
# Wrapping the prespective based on the transformation matrix
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
 
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)