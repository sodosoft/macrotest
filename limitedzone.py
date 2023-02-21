import re
import pyautogui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox   
import configparser
# pip install numpy
from datetime import datetime
from PIL import ImageGrab
import pytesseract
import clipboard

win = Tk ()
win.title("HD DEMO")
win.geometry('300x150')

def btnClick():
    position(1017, 675, 1053,694)
    
    
    position(1017, 699, 1053,718)
    
    position(1017, 725, 1053,741)    
   
    position(1017, 768, 1053,787)  
    
def position(a,b,c,d):
    img = ImageGrab.grab((a,b,c,d))   

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img)
    new_str = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", text)
    print(new_str) 

    clipboard.copy(new_str)
    pyautogui.moveTo(a + 55, b + 10)
    pyautogui.click()  
    pyautogui.hotkey('ctrl','v')
    pyautogui.moveTo(a + 100, b + 10)
    pyautogui.press('enter')


action=ttk.Button(win, text="test", command=btnClick)
action.grid(column=0, row=1)
win.mainloop()