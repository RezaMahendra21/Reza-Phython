import os
import cv2, numpy as np
from PIL import Image
# os.system("clear")

dataPath = 'D:/Coding/Python_APP/Face-Recognition1/4_Face_Recognition/dataface/'
facesDetector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# imgPaths = [os.path.join(dataPath, f) for f in os.listdir(dataPath)]
# for imagePath in imgPaths :
    # faceID = int(os.path.split(imagePath)[1].split(".")[2])
    # faceID = int(os.path.split(imagePath)[-1].split(".")[2])
    # print("ini", int(os.path.split(imagePath)[-1].split(".")[2]))
    # print("--")
    # print(faceID)
# print(imgPaths, "\n")
# print(cv2.__file__)
# exit()

"""
    path pada imgPath
    exmpl :
    face.1.2.jpg
    face => index 0, 1 index ke 1, 2 index ke 2, jpg index ke 3 atau ke -1
    int(os.path.split(imagePath)[-1].split(".")[1])
    -1 => face.1.1
    1 => id gambar 

"""

def getImageLabel(path):
    imgPaths = [os.path.join(path, f) for f in os.listdir(path) ]
    faceSamples = []
    faceIDs = []
    i = 1
    # print(imgPaths)
    for imagePath in imgPaths :
        PILImg = Image.open(imagePath).convert('L') # convert ke Grey
        imgNum = np.array(PILImg, 'uint8')
        faceID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = facesDetector.detectMultiScale(imgNum)
        # print("ke : ", imagePath.split(".")[1])
        print(faceID, "ke : ", i)
        i += 1
        for (x,y,w,h) in faces :
            faceSamples.append(imgNum[y:y+h, x:x+w])
            faceIDs.append(faceID)
        # print(faceIDs)
    return faceSamples, faceIDs

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

print("Strat training face data")
faces, IDs = getImageLabel(dataPath)
faceRecognizer.train(faces, np.array(IDs))
# save model training
faceRecognizer.write('./4_Face_Recognition/my_faces.xml')
print(f"data has trained and saved")
