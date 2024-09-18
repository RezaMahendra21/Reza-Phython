import cv2
import datetime as dt
import uuid
import os

# idFace = dt.datetime.now().strftime ("%d%H%M%S")
idFace = input('Masukkan id ........')

faceDetector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
countImg = 1
dirImg = 'dataface'


while True :
    status, frameImg = cam.read()
    greyImg = cv2.cvtColor(src=frameImg, code=cv2.COLOR_BGR2GRAY)

    # haarcascade
    face = faceDetector.detectMultiScale(greyImg, 1.3, 5)
    for (x,y,h,w) in face :
        frameImg = cv2.rectangle(frameImg, (x,y), (x+h, y+w), (255,0,0), 2)
        imgName = "face." + idFace + "." + str(countImg) + ".jpg"
        path = 'D:/Coding/Python_APP/Face-Recognition1/4_Face_Recognition/dataface'
        cv2.imwrite(os.path.join(path, imgName), frameImg)
        print(imgName)
    countImg += 1
    # print(countImg)
    cv2.imshow("Me", frameImg)
    key = cv2.waitKey(1) & 0xff
    keyEsc = 27
    if key == keyEsc or key == ord('q') :
        break
    elif countImg  > 30 :
        break

cam.release()
cv2.destroyAllWindows()