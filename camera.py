import cv2
import pytesseract as pyt

img = cv2.imread("crop.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret, thresh_value = cv2.threshold(gray,90,255,cv2.THRESH_BINARY_INV)

pyt.pytesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print(pyt.image_to_string(thresh_value, lang='eng'))
#cv2.imshow("Result", thresh_value)
#cv2.waitKey(0)