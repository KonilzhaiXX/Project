import pytesseract as pyt
import cv2
import re


def replace_chars(text):
    pyt.pytesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    list_of_numbers = re.findall(r'\d+', text)
    result_number = ''.join(list_of_numbers)
    return result_number

def qwe():
    img = cv2.imread('image.jpg')
    x, y, w, h = 32, 180, 576, 87
    try:
        crop = img[y: y + h, x: x + w]
        cv2.imwrite("crop.jpg", crop)
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        ret,thresh_value = cv2.threshold(gray,80,255,cv2.THRESH_BINARY_INV)
        cv2.imwrite("1.jpg", thresh_value) 
        ocr = pyt.image_to_string(thresh_value, lang='eng')
    except:
        return "Error"
    return replace_chars(ocr)
