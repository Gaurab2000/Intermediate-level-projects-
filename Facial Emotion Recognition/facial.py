import os
import cv2
import numpy as np

FaceCascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap=cv2.VideoCapture(0)
if not (cap.isOpened()):
    print("cam could not be opened")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,300)


while(True):
        ret,frame=cap.read()


        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces = FaceCascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)


        for (x, y, w, h) in faces:

           
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)  #BGR, 

        cv2.imshow('frames',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()