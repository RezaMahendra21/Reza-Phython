
import cv2
import os
import numpy as np

os.system("clear")

myPhoto = cv2.imread("./19_PCD/me.jpg")

# Channel Color
blueChn = myPhoto[:, :, 0]
greenChn = myPhoto[:, :, 1]
redChn = myPhoto[:, :, 2]

# stat myPhoto
# imgRow = len(myPhoto)
# imgCol = len(myPhoto[0])

# Gambar baru dengan nilai 0
# np.uint8 mengubah integer menjadi unsigned integer (0-255)
# grayImage = np.zeros((imgRow, imgCol), dtype=np.uint8)

# for row in range(len(myPhoto)) :
#     for col in range(len(myPhoto[0])) :
#         grayImage[row, col] = 0.299 * redChn[row, col] + 0.587 * greenChn[row, col] + 0.114 * blueChn[row, col]

# cv2.imshow("RGB2Gray", grayImage)
# cv2.waitKey()

# blueChn,greenChn,redChn = cv2.split(myPhoto)



# Conversi to Gray Scale menggunakan Open CV
# myPhotoInGray = cv2.cvtColor(myPhoto, cv2.COLOR_BGR2GRAY)
# cv2.imshow("me in RGB", myPhoto)
# cv2.imshow("me in Gray", myPhotoInGray)
# cv2.waitKey()