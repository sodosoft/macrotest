import pyautogui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox   

from datetime import datetime

now  = datetime.now()
print("현재 :", now)	# 현재 : 2021-01-09 21:30:12.050111

date_to_compare = datetime.strptime("20240315", "%Y%m%d")
print("비교할 날짜 :", date_to_compare)	# 비교할 날짜 : 2024-03-15 00:00:00

date_diff = now - date_to_compare
print("차이 :", date_diff)	# 차이 : 1

enable = True

if(date_diff < 6):
    messagebox.showinfo("프로그램 만기일",date_diff + "일 남았습니다.\n제조사에 문의 부탁드립니다.")
elif(date_diff < 0):
    messagebox.showinfo("프로그램 만기일",date_diff + "일 지났습니다.\n제조사에 문의 부탁드립니다.")
    enable = False
# pip install numpy

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
    
    img = ImageGrab.grab((754,300,962,686))   
    # img.save("D:/test4.png")    
    img.save("c://images//test4.png")   
    # img = ImageGrab.grab((945,463,979,480))   
    # img.save("D:/test5.png")    

def btnClick2():
    from PIL import Image
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open("D:\\다운로드.png"))

    text2 = text.split('\n')
    cnt = len(text2)
    result = list()

    for i in range(15):
        if '~' not in text2[i] and len(text2[i]) > 1 and len(text2[i]) < 4:  
                        
            result.append(text2[i])   

        with open("D:\\new.txt", "w", encoding="utf8") as f:       
            f.write(result)
            f.write("\n")
            f.write(result.replace(" ", ""))
        
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
action2=ttk.Button(win, text="추출", command=btnClick2)
action2.grid(column=0, row=4)
win.mainloop()


    



# btn = Button(tk, text= "Start", fg= "blue", command = btnClick)
# btn.pack(side=LEFT, padx=10, pady = 10)

# tk.mainloop()




