# import the necessary packages
import numpy as np
import cv2
import os 
from os import path

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
	# initialize the dimensions of the image to be resized and
	# grab the image size
	dim = None
	(h, w) = image.shape[:2]

	# if both the width and height are None, then return the
	# original image
	if width is None and height is None:
		return image

	# check to see if the width is None
	if width is None:
		# calculate the ratio of the height and construct the
       	# dimensions
		r = height / float(h)
		dim = (int(w * r), height)

    # otherwise, the height is None
	else:
		# calculate the ratio of the width and construct the
   		# dimensions
		r = width / float(w)
		dim = (width, int(h * r))

	# resize the image
	resized = cv2.resize(image, dim, interpolation = inter)

   	# return the resized image
	return resized
def heat(hi,li,temp):
	# load the image
	basepath = os.getcwd()
	r=hi-li
	gray=int(float(((temp-li)/r))*255)
	print("".join([basepath,"\simulation\static\images\input.jpeg"]))
	img = cv2.imread("".join([basepath,"\simulation\static\images\input.jpeg"]))
	imgre=image_resize(img,600,1000)
	cv2.imwrite("".join([basepath,"\simulation\static\images\input.jpeg"]),imgre)
	out=img.copy()
	imgg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret,th = cv2.threshold(imgg,gray,255,cv2.THRESH_BINARY)
	contours, hierarchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	for i in contours:
		if(cv2.contourArea(i,True)<-100):
			x,y,w,h = cv2.boundingRect(i)
			cv2.rectangle(out,(x,y),(x+w,y+h),(0,0,0),int(img.shape[0]*0.007))
	cv2.imwrite("".join([basepath,"\simulation\static\images\output.jpeg"]),image_resize(out,600,1000))