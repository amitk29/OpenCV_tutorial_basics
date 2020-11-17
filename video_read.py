import cv2 as cv

capture=cv.VideoCapture(0)

while True:
    isTrue, frame=capture.read()  #read frame by frame, is True returns whether succesfully readed or not
    cv.imshow('Video',frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release() #releasing capture variable
cv.destroyAllWindows()

