import pyautogui as pg
import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
import clipboard
import time

# button5location = pg.locateOnScreen('D:/green.png')# 이미지가 있는 위치를 가져옵니다. 
# print(button5location)  

for idx, i in enumerate(pg.locateAllOnScreen("D:/green3.png"), start=1):

    # if idx == 2: # 2번쨰 등장하는 형상에만 동작 *참고 : start=1

    print(i.left, i.top)  

    if(i != None):
        startX =  i.left + 132   
        startY =  i.top

        # 캡쳐 구간
        img = ImageGrab.grab((startX, startY, startX + 35 ,startY + 18))   
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(img)

        print(text) 
        
        clipboard.copy(text)
        pg.moveTo(startX + 40, startY)
        pg.click()  
        pg.hotkey('ctrl','v')
        # pg.moveTo(startX + 10,startY + 180)    
        # pg.click()  
        time.sleep(0.5)
# img = cv2.imread('D:/colorTest.png')
# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# bound_lower = np.array([25, 20, 20])
# bound_upper = np.array([100, 255, 255])

# mask_green = cv2.inRange(hsv_img, bound_lower, bound_upper)
# kernel = np.ones((7,7),np.uint8)

# mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)
# mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

# seg_img = cv2.bitwise_and(img, img, mask=mask_green)
# contours, hier = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# output = cv2.drawContours(seg_img, contours, -1, (0, 0, 255), 3)

# cv2.imshow("Result", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()