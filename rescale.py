import cv2 as cv

capture=cv.VideoCapture(0)

def rescaleFrame(frame,scale=0.5): #will work for all: videos,images,live videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]* scale)

    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

while True:
    isTrue,frame=capture.read()
    rescaled_frame=rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Rescaled Video',rescaled_frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
