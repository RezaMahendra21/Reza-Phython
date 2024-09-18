# opencv
import cv2
# import tensorflow.python.keras.

# img = cv.imread("./me.jpg")
# cv.imshow("OK", img)
# cv.waitKey()

# cv2.ocl.setUseOpenCL(False)
cap = cv2.VideoCapture(0)
while True :
    retV , frame = cap.read()
    # print(retV) # status
    # print(frame) # fps ==> image persecond
    cv2.imshow("ANd", frame)
    key = cv2.waitKey(1) & 0xff
    btnEsc = 27
    if key == ord('q') or key == btnEsc :
        break
cap.release()
cv2.destroyAllWindows()