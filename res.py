import cv2
import matplotlib.pyplot as pl

img = cv2.imread("image.jpg")

cv2.imshow("original", img)

roi = cv2.selectROI(windowName="original", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi

print(roi) 

if roi != (0,0,0,0):
    crop = img[y:y+h, x:x+w]
    cv2.imshow("crop", crop)
    cv2.imwrite("crop.jpg", crop)
    print("Saved!")
cv2.waitKey(0)
cv2.destroyAllWindows()