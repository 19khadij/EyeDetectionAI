print("Press \'s\' to destroy the webcam!")

import numpy as np
import cv2

eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

web_cam=cv2.VideoCapture(0)
while 1:
    success,image=web_cam.read()#boolean type variable (True & false)
    imagegray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(imagegray,3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,37,45),2)
        cv2.putText(image,"FACE",(x,y-5),cv2.FONT_HERSHEY_PLAIN,2.5,(0,255,0),2)

        #eye detection code
        crop_imagegray=imagegray[y:y+h,x:x+w]
        crop_image=image[y:y+h,x:x+w]
        eye=eye_cascade.detectMultiScale(crop_imagegray)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(crop_image,(ex,ey),(ex+ew,ey+eh),(255,45,89),2)
            cv2.putText(crop_image,"EYE",(ex,ey-5),cv2.FONT_HERSHEY_PLAIN,1.5,(0,45,100),2)
    


    cv2.imshow("webcamcapture",image)
    if cv2.waitKey(10)&0xff==ord('s'):
        break

web_cam.release()
cv2.destroyAllWindows()

