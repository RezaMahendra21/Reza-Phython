import cv2
import os

os.system("clear")

citra = cv2.imread("./19_PCD/me.jpg")

# Python warna = B-G-R
# Channel semua warna
# print(citra)

# Channel Blue
# print("Channel Warna Blue")
# print(citra[:, :, 0])

# Channel Green
# print("Channel Warna Green")
# print(citra[:, :, 1])

# Channel Red
# print("Channel RED")
# print("OK")
# print(citra[:, :, 2])

# cv2.imshow("Me", citra)
# cv2.imshow("Me Blue", citra[:, :, 0])
# cv2.imshow("Me Green", citra[:, :, 1])
# cv2.imshow("Me RED", citra[:, :, 2])
# menampilkan satu Channel Warna akan menjadi Grayscale


cv2.waitKey()
