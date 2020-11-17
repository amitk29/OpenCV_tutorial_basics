import cv2 as cv
import numpy as np

img=cv.imread('i.png')
cv.imshow('Picture',img)

## Converting to GrayScale
#gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Grayscale',gray)


## blur

#blur=cv.blur(img,(5,5),borderType=cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

## Edge Cascade

#canny=cv.Canny(img,125,175)
#cv.imshow('Canny Edges',canny)

##Resize

#resized=cv.resize(img,(250,250),interpolation=cv.INTER_AREA)
#cv.imshow('Resized',resized)

##crop
cropped=img[50:200,200:400]
cv.imshow('cropped',cropped)



cv.waitKey(0)