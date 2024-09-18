import cv2, numpy as np
from PIL import Image

cam = cv2.VideoCapture(0)
cam.set(3, 640) # width
cam.set(4, 480)

faceDetector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

faceRecognizer.read('./4_Face_Recognition/my_faces.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
names = ['Unknown', 'Andrian', 'Cimen']
minWidth = 0.1*cam.get(3)
minHeight = 0.1*cam.get(4)

while True :
    status, frameImg = cam.read()
    frameImg = cv2.flip(frameImg, 1)
    greyImg = cv2.cvtColor(src=frameImg, code=cv2.COLOR_BGR2GRAY)
    # haarcascade
    faces = faceDetector.detectMultiScale(greyImg, 1.2, 5, minSize=(round(minWidth), round(minHeight)))
    for (x,y,h,w) in faces :
        frameImg = cv2.rectangle(frameImg, (x,y), (x+h, y+w), (255,0,0), 2)
        id, confidence = faceRecognizer.predict(greyImg[y:y+h, x:x+w]) # confidence 0 cocok sempurna
        if confidence < 50 :
            nameId = names[id]
            confidenceTxt = "{0}%".format(round(100-confidence))
        else :
            nameId = names[0]
            confidenceTxt = "{0}%".format(round(100-confidence))
        cv2.putText(frameImg, str(nameId), (x+5, y-5), font, 1, (255,255,255), 2)
        cv2.putText(frameImg, str(confidenceTxt), (x+5, y+h-5), font, 1, (255,255,0), 1)
    # print(countImg)
    cv2.imshow("Me", frameImg)
    key = cv2.waitKey(1) & 0xff
    keyEsc = 27
    if key == keyEsc or key == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()