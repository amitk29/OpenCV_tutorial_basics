import cv2 as cv
import numpy as np

#img =cv.imread('i.png')
#cv.imshow('Img',img)

blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

##paint image a certain colour
#blank[:]=0,255,0
#cv.imshow('Green',blank)

#blank[200:300,300:400]=0,0,255
#cv.imshow('Blue',blank)

##plotting a rectangle

#cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)
#cv.imshow('Rect',blank)

## Drawing a circle

#cv.circle(blank,(250,250),40,color=(0,0,255),thickness=-1)
#cv.imshow('Circle',blank)

##Draw a line

#cv.line(blank,(250,250),(260,270),(0,0,255),thickness=2)
#cv.imshow('Line',blank)

##write text

cv.putText(blank,'I am Amit', color=(255,0,0),thickness=2,org=(100,250),fontFace=cv.FONT_HERSHEY_TRIPLEX,fontScale=2)
cv.imshow('Image_text',blank)



cv.waitKey(0)