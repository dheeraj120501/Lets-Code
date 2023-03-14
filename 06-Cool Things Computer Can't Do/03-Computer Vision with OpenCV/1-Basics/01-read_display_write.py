#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
# Loading or Reading the image from disk
# returns a NumPy array representing the image
# img is basically an array of pixels, we can simply use the shape attribute that contains the height, width, and the number of channels.
# we also have cv.imwrite(path, img) to save the image on disk

cv.imshow('Cats', img)
# Showing the image in a new window

cv.waitKey(0)
# cv2.waitKey pauses the execution of the script until we press a key on our keyboard. 
# Using a parameter of 0 indicates that any keypress will un-pause the execution.

capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
# Reading Videos (sequence of images)
# Going through each frame of video and then displaying it fast so it look like a video is displayed

while True:
    frame_status, frame = capture.read()

    if frame_status:    
    # This is the preferred way - if `frame_status` is false (the frame could not be read, or we're at the end of the video), we immediately break from the loop. 
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()