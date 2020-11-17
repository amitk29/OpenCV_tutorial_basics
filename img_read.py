import cv2 as cv

img=cv.imread('i.png')

#cv.namedWindow( "Img", cv.WINDOW_AUTOSIZE )

cv.imshow('Img',img)
cv.waitKey(0)