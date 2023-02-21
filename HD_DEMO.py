import sys
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
import time

now  = datetime.now()
print("현재 :", now)	# 현재 : 2021-01-09 21:30:12.050111

date_to_compare = datetime.strptime("20240401", "%Y%m%d")
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

def config_read():
    # 설정파일 읽기
    config = configparser.ConfigParser()    
    config.read('config.ini', encoding='utf-8') 
    positionStrX = config['position']['X']
    positionStrY = config['position']['Y']

positionStr = ''
win = Tk ()
win.title("HD DEMO")
win.iconbitmap('macro.ico')
win.geometry('300x150')

# 설정파일 읽기
config = configparser.ConfigParser()    
config.read('config.ini', encoding='utf-8') 
positionStrX = int(config['position']['X'])
positionStrY = int(config['position']['Y'])
myIP = str(config['system']['IP'])

if(myIP == "192.168.45.214"):    
    def setting():
        # myScreenshot = pyautogui.screenShot(pip )
        # myScreenshot.save('D:/test2.png')
        #  messagebox.showinfo("mouse position", pyautogui.position())
        # pyautogui.onScreen('D:/test3.png',region=(3187,462,20,30))
        from PIL import ImageGrab       
        import pytesseract
        
        # 설정파일 읽기
        config = configparser.ConfigParser()    
        config.read('config.ini', encoding='utf-8') 
        positionStrX = int(config['position']['X'])
        positionStrY = int(config['position']['Y'])
        print(positionStrX)
        print(positionStrY)
        
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
        
        messagebox.showinfo("추출 문자",result)
        
    def clickMe():
        # myScreenshot = pyautogui.screenShot(pip )
        # myScreenshot.save('D:/test2.png')
        #  messagebox.showinfo("mouse position", pyautogui.position())
        # pyautogui.onScreen('D:/test3.png',region=(3187,462,20,30))
        
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
        
        # 1
        for i in range(5):
            clipboard.copy(result[i])
            # 색확인 필요?
            pyautogui.moveTo(positionStrX + 79,positionStrY + 13 + (22 * i))
            pyautogui.click()  
            pyautogui.hotkey('ctrl','v')
            # pyautogui.rightClick()  
            # # clipboard.paste()
            # pyautogui.moveTo(positionStrX + 108,positionStrY + 180 + (22 * i))    
            # pyautogui.click()  
            time.sleep(0.5)
        # img.save("D:/test4.png")    
        
        # img = ImageGrab.grab((945,463,979,480))   
        # img.save("D:/test5.png")    
        sys.exit()
    def color_def() : 
        #red / green / blue pre-define
        red = (191,19,32)
        green = (33,176,76)
        blue = (0,0,255)

        #screen-shot
        screen = ImageGrab.grab()

        #get current position and rgb
        pyautogui.moveTo(525, 486)
        pos = pyautogui.position()
        print(pos)
        rgb = screen.getpixel(pos)

        if rgb == red : print("red")
        elif rgb == green : print("green")
        elif rgb == blue : print("blue")
        else : print("알 수 없음")   
    def btnClick2():
        import subprocess

        subprocess.Popen('HDDEMO.exe')
            
    def btnClick():
        sys.exit()
        
    def btnColorClick():
        for idx, i in enumerate(pyautogui.locateAllOnScreen("D:/green3.png"), start=1):

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
                pyautogui.moveTo(startX + 40, startY)
                pyautogui.click()  
                pyautogui.hotkey('ctrl','v')
                # pg.moveTo(startX + 10,startY + 180)    
                # pg.click()  
                # time.sleep(0.5)
        
    label = ttk.Label(text = '기준 좌표를 확인하세요 ')
    label.grid(column = 0, row = 0)  
    action=ttk.Button(win, text="좌표 확인", command=btnClick2)
    action.grid(column=0, row=1)
    action=ttk.Button(win, text="설정 확인", command=setting)
    action.grid(column=0, row=2)
    action1=ttk.Button(win, text="작업", command=clickMe)
    action1.grid(column=0, row=3)
    if(enable):
        action1.configure(state='enabled')
    else:
        action1.configure(state='disabled')
    action4=ttk.Button(win, text="색깔", command=color_def)
    action4.grid(column=0, row=4)    
    action3=ttk.Button(win, text="종료", command=btnClick)
    action3.grid(column=0, row=5)
    # action3=ttk.Button(win, text="추출", command=btnClick2)
    # action3.grid(column=0, row=3)
    
    win.mainloop()
else:
    messagebox.showwarning("계약 위반", "지정 IP가 아닙니다.\n제조사에 문의 부탁드립니다.")
    sys.exit()




    


# pyinstaller -w -F --icon=macro.ico HD_DEMO.py
# btn = Button(tk, text= "Start", fg= "blue", command = btnClick)
# btn.pack(side=LEFT, padx=10, pady = 10)

# tk.mainloop()








