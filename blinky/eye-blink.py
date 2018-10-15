import cv2
from firebase import motiondetect

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascase-eye.xml')

cap = cv2.VideoCapture(0)
c=0

while(cap.isOpened()):  # check !
    # capture frame-by-frame
    ret, img = cap.read()

    if ret: # check ! (some webcam's need a "warmup")
        # our operation on frame come here
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        k=1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            k=0
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        if(k==1):
            t="You are Blinking!",c
            motiondetect("Blinked!")
            c=c+1
            print(t)



    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
'''
    while cv2.getWindowProperty('window-name', 0) >= 0:
        keyCode = cv2.waitKey(50)
'''
cap.release()
cv2.destroyAllWindows()
