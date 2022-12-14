import cv2
import numpy as np
web=cv2.VideoCapture(0)
web.set(3,640) #width, 3 is the id for width
web.set(4,480)# height, 4 is the id for heght
web.set(10,100)#brightness, 10 is the id for brightness
while True:
    success, img=web.read()
    cv2.imshow("Webcam",img)
    #img1 = cv2.imread(r"C:\Users\chaud\Desktop\rubik.jpg")
    #img=cv2.resize(img1,(300,200))
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,146,94])
    upper_red=np.array([5,255,255])
    lower_orange=np.array([7,226,145])
    upper_orange=np.array([17,255,255])
    lower_yellow=np.array([24,160,150])
    upper_yellow=np.array([29,255,255])
    lower_green=np.array([31,69,61])
    upper_green=np.array([69,255,250])
    lower_blue=np.array([43,116,69])
    upper_blue=np.array([128,238,214])
    mask_red=cv2.inRange(imgHSV,lower_red,upper_red)
    mask_orange=cv2.inRange(imgHSV,lower_orange,upper_orange)
    mask_yellow=cv2.inRange(imgHSV,lower_yellow,upper_yellow)
    mask_green=cv2.inRange(imgHSV,lower_green,upper_green)
    mask_blue=cv2.inRange(imgHSV,lower_blue,upper_blue)
    imgResult_yellow=cv2.bitwise_and(img,img,mask=mask_yellow)
    imgResult_blue=cv2.bitwise_and(img,img,mask=mask_blue)
    imgResult_Red=cv2.bitwise_and(img,img,mask=mask_red)
    imgResult_Orange=cv2.bitwise_and(img,img,mask=mask_orange)
    imgResult_green=cv2.bitwise_and(img,img,mask=mask_green)
    imgResult1=cv2.bitwise_or(imgResult_Red,imgResult_Orange,imgResult_yellow,mask=None)
    imgResult=cv2.bitwise_or(imgResult1,imgResult_green,imgResult_blue,mask=None)
    cv2.imshow("img",imgResult_yellow)
    cv2.imshow("img1",imgResult_blue)
    cv2.imshow("Real_image",imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
