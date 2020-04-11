#importing all the required package
import numpy as np
import cv2

#image name here image and py file are in same folder
img = "photo.jpg"

img_obj = cv2.imread(img)

#img_obj.shape   -- to check the shape of image 

scale_percent = 0.60
width = int(img_obj.shape[1]*scale_percent)
height = int(img_obj.shape[0]*scale_percent)

dim = (width,height)
resized = cv2.resize(img_obj,dim,interpolation = cv2.INTER_AREA)  # resizing the image 

kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])
sharpened = cv2.filter2D(resized,-1,kernel_sharpening)   # shape the image


gray = cv2.cvtColor(sharpened , cv2.COLOR_BGR2GRAY)      # convert in black and white 
object_detection = cv2.cvtColor(sharpened, cv2.COLOR_BGR2HSV )  #convert in image detection formate


inv = 255-gray					# convert in inverse form 
gauss = cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0,sigmaY=0)  # convert in gauss form 


pencil = cv2.divide(gray,255-gauss,scale=256)

# to display these four images 
cv2.imshow('resized',resized)
cv2.imshow('sharp',sharpened)
cv2.imshow("gray", gray)
cv2.imshow('pencile',pencil)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Here u can save the image , that formate you want.Here, image will save at the same path of code file 

# cv2.imwrite("pencil_sketch.jpg",pencil)


## Thanks 