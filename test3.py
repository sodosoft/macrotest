import pyautogui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox   
import configparser
# pip install numpy
from datetime import datetime

now  = datetime.now()
print("현재 :", now)	# 현재 : 2021-01-09 21:30:12.050111

date_to_compare = datetime.strptime("20230212", "%Y%m%d")
print("비교할 날짜 :", date_to_compare)	# 비교할 날짜 : 2024-03-15 00:00:00

date_diff = date_to_compare - now
print("차이 :", date_diff)	# 차이 : 1

dateval1 = date_diff.days

enable = True

if(dateval1< 0):
    messagebox.showinfo("프로그램 만기일", str(dateval1) + "일 지났습니다.\n제조사에 문의 부탁드립니다.")
    enable = False
elif(dateval1< 6):
    messagebox.showinfo("프로그램 만기일", str(dateval1) + "일 남았습니다.\n제조사에 문의 부탁드립니다.")
   
    
positionStrX = 0
positionStrY = 0

def config_read():
    # 설정파일 읽기
    config = configparser.ConfigParser()    
    config.read('config.ini', encoding='utf-8') 
    positionStrX = config['position']['X']
    positionStrY = config['position']['Y']

positionStr = ''
win = Tk ()
win.title("HD DEMO")
win.geometry('300x500')
def clickMe():
    # myScreenshot = pyautogui.screenShot(pip )
    # myScreenshot.save('D:/test2.png')
    #  messagebox.showinfo("mouse position", pyautogui.position())
    # pyautogui.onScreen('D:/test3.png',region=(3187,462,20,30))
    from PIL import ImageGrab
    import pytesseract
    
    
    
    
    # 캡쳐 구간
    img = ImageGrab.grab((positionStrX,positionStrY,positionStrX + 53,positionStrY + 345))   
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img)
    
    
    text2 = text.split('\n')
    cnt = len(text2)
    result = list()
    for i in range(15):
        if '~' not in text2[i] and len(text2[i]) > 1 and len(text2[i]) < 4:  
                        
            result.append(text2[i])   
            
    print(result)
    
    import clipboard
    import time
    
    messagebox.showinfo("추출 문자",result)
    # 1
    for i in range(5):
        clipboard.copy(result[i])
        pyautogui.moveTo(positionStrX + 79,positionStrY + 13 + (22 * i))
        pyautogui.rightClick()  
        # clipboard.paste()
        pyautogui.moveTo(positionStrX + 108,positionStrY + 180 + (22 * i))    
        pyautogui.click()  
        time.sleep(1)
    # img.save("D:/test4.png")    
    
    # img = ImageGrab.grab((945,463,979,480))   
    # img.save("D:/test5.png")    

def btnClick2():
    from PIL import Image
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open("D:\\test4.png"))

    text2 = text.split('\n')
    cnt = len(text2)
    result = list()

    for i in range(15):
        if '~' not in text2[i] and len(text2[i]) > 1 and len(text2[i]) < 4:  
                        
            result.append(text2[i])   
            
    print(result)
    messagebox.showinfo("추출 문자",result)
        
def btnClick():
    
    pyautogui.moveTo(59,148)
    pyautogui.drag(15,0, duration=0.25)
    pyautogui.rightClick()
    pyautogui.moveTo(59,148)

    pyautogui.moveTo(106,162)
    pyautogui.click()

    pyautogui.moveTo(180,142)
    pyautogui.click()
    pyautogui.rightClick()
    pyautogui.moveTo(262,306)
    pyautogui.click()   
label = ttk.Label(text = '기준 좌표 : ')
label.grid(column = 0, row = 0)  
str = StringVar()
textbox = ttk.Entry(win, width=20, textvariable=str)
textbox.grid(column = 0 , row = 1)
action1=ttk.Button(win, text="capture", command=clickMe)
action1.grid(column=0, row=2)
action2=ttk.Button(win, text="Start", command=btnClick)
action2.grid(column=0, row=3)
if(enable):
    action2.configure(state='enabled')
else:
    action2.configure(state='disabled')
action2=ttk.Button(win, text="추출", command=btnClick2)
action2.grid(column=0, row=4)
win.mainloop()


    



# btn = Button(tk, text= "Start", fg= "blue", command = btnClick)
# btn.pack(side=LEFT, padx=10, pady = 10)

# tk.mainloop()








