import cv2 
import numpy as np 

def stackImages(scale, imgArray): 
    # Number of rows of stacked images wanted
    rows = len(imgArray) 
    # Number of columns of stacked images wanted
    cols = len(imgArray[0]) 
    # check if we are provided by a list of image or not
    rowsAvailable = isinstance(imgArray[0], list) 
    # width of every image
    width = imgArray[0][0].shape[1] 
    # height of every image
    height = imgArray[0][0].shape[0] 
    
    # If the list of image is provided
    if rowsAvailable: 
        # loop through entire imgArray
        for x in range (0, rows): 
            for y in range(0, cols): 
                # check if the size of other images in the array/matrix is same as that of the first image or not if not resize them to that of the first image
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]: 
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale) 
                else: 
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                # check if image is grayScale or not if length of shape is 2 then we have only one channel grayscale so we change the image's color space to BGR 
                if len(imgArray[x][y].shape) == 2: 
                    imgArray[x][y]= cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        # Create an empty black canvas as every pixel in that array/matrix is zero(Black pixel) 
        imageBlank = np.zeros((height, width, 3), np.uint8) 
        hor = [imageBlank]*rows 
        hor_con = [imageBlank]*rows 
        for x in range(0, rows): 
            hor[x] = np.hstack(imgArray[x]) 
        ver = np.vstack(hor) 
    else: 
        for x in range(0, rows): 
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]: 
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale) 
            else: 
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale) 
            if len(imgArray[x].shape) == 2: 
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR) 
        hor= np.hstack(imgArray) 
        ver = hor 
    return ver 

img = cv2.imread('../Resources/Photos/cat.jpg') 
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

# hstack and vstack are the functions of numpy, we just extend the arrays making it stacked images.
# NOTE: Here the color space of the images should be same.
# imgHor = np.hstack((img,img)) 
# imgVer = np.vstack((img,img)) 
# cv2.imshow("Horizontal",imgHor) 
# cv2.imshow("Vertical",imgVer) 

# With stack images color space need not to be same.
imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img])) 

cv2.imshow("ImageStack",imgStack) 
cv2.waitKey(0)