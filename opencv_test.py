#!/usr/bin/python3
#打开摄像头，每3秒取一帧，并显示，以数字保存在/mnt/hgfs/vmware_shared/
import cv2
capture = cv2.VideoCapture(0)
num=1
while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # cv2.imshow('frame', gray)
    cv2.imshow('frame',frame)
    pathname='/mnt/hgfs/vmware_shared/'+str(num)+'.jpg'
    cv2.imwrite(pathname,frame)
    num=num+1
    if cv2.waitKey(3000) == ord('q'):
        break