# import opencv
import numpy
import cv2

# print(cv2.__file__)
# exit()

# open camera
cam = cv2.VideoCapture(0)
# set camera display
cam.set(3, 640) # width camera
cam.set(4, 480) # height camera

# detection face
# faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceDetector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


while True :
    # start camera
    retStatus, imgFrame = cam.read()
    if not retStatus :
        break
    greyImg = cv2.cvtColor(imgFrame, cv2.COLOR_BGR2GRAY)

    # detection face
    face = faceDetector.detectMultiScale(greyImg, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in face :
        imgFrame = cv2.rectangle(img=imgFrame, pt1=(x,y), pt2=(x+w, y+h), color=(0,255,0), thickness=2)
    
    cv2.imshow("Me", imgFrame)
    key = cv2.waitKey(1) & 0xff
    keyEsc = 27
    if key == keyEsc or key == ord('q') :
        break
cam.release()
cv2.destroyAllWindows()