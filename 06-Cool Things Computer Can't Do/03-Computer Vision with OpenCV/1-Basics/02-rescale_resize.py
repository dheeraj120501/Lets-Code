#pylint:disable=no-member
import cv2 as cv

# img = cv.imread('../Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Works with Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Works with live video
    capture.set(3,width)
    capture.set(4,height)
    
# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    frame_status, frame = capture.read()

    resized_frame = rescaleFrame(frame, scale=.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', resized_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()