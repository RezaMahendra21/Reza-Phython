import cv2

cam = cv2.VideoCapture(0)
eyeDetection = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
faceDetection = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# smileDetection = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

while True :
    status, imgFrame = cam.read()
    imgGrey = cv2.cvtColor(imgFrame, cv2.COLOR_BGR2GRAY)

    # haarcascade
    eye = eyeDetection.detectMultiScale(imgGrey, 1.3, 5)
    face = faceDetection.detectMultiScale(imgGrey, 1.3, 5)
    # smile = smileDetection.detectMultiScale(imgGrey, 1.3, 5)

    # object capture
    for (x,y,w,h) in eye :
        imgFrame = cv2.rectangle(imgFrame, (x,y), (x+h, y+w), (192,255,0), 2)
    for (x,y,w,h) in face :
        imgFrame = cv2.rectangle(imgFrame, (x,y), (x+w, y+h), (255,0,0), 1)
    # for (x,y,w,h) in smile :
    #     imgFrame = cv2.rectangle(imgFrame, (x,y), (x+w, y+h), (0,0,242), 4)
    
    cv2.imshow("Me", imgFrame)
    key = cv2.waitKey(1) & 0xff
    keyEsc = 27
    if key == keyEsc or key == ord('q') :
        break
cam.release()
cv2.destroyAllWindows()
