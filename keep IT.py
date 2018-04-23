#import
#============================================================================
import tkinter as tk
import csv
import time
import random
from PIL import Image,ImageTk
from tkinter import messagebox

#constan
#===========================================================================ๅๅ
LARGE_FONT = ("console", 16)
LARGE_FONT2 = ("console", 20)

class keepit(tk.Tk):
    # keep  สร้าง class  หน้าต่างหลักของการทำงาน
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)



        load = Image.open("light.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self,image=rende)
        img1 = tk.PhotoImage(file="light.png")
        img.image = rende


        self.tk.call('wm', 'iconphoto', self, img1)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # frames is == dic
        self.frames = {}

        # loop StartPage Page one,tow,Three and pange four

        for F in (StartPage, PageOne, PageTwo,PageThree,PageFour):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # show_frame is method display frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# class StartPage main frame
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("Feame_bgfirst.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rende)
        img.image = rende
        img.pack()

        keep1 = Image.open("keep.png")      #lode image name "keep.png"

        butkeep = ImageTk.PhotoImage(keep1)

        but1 = tk.Button(self, text="จำได้",width=8 ,font=LARGE_FONT,command=lambda: controller.show_frame(PageOne))
        but1.place(x=70,y=450)

        but2 = tk.Button(self, text="ยังจำไม่ได้",width=8 , font=LARGE_FONT,command=lambda: controller.show_frame(PageTwo))
        but2.place(x=190,y=450)

        but3 = tk.Button(self, text="ทดสอบ",width=8, font=LARGE_FONT,command=lambda: controller.show_frame(PageThree))
        but3.place(x=310,y=450)

        but4 = tk.Button(self, text="เพิ่มคําศัพท์", width=8, font=LARGE_FONT,command=lambda: controller.show_frame(PageFour))
        but4.place(x=70,y=500)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ยังจำได้", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ยังจำไม่ได้", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ทดสอบ", font = LARGE_FONT2)
        label.pack(pady=10, padx=10)
        frame1 = tk.Frame(self)
        frame1.place(x=100, y= 100)
        resultstrin = read_csv_file()

        text = tk.Button(frame1, text="คำถาม",font = LARGE_FONT2)
        text.pack()

        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageFour(tk.Frame):       # adding word  q

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        text1 = tk.StringVar()
        text2 = tk.StringVar()

        load = Image.open("Feame_bg.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rende)
        img.image = rende
        img.pack()

        label = tk.Label(self, text="เพิ่มคำศัทพ์", font=LARGE_FONT)
        label.pack()

        label2 = tk.Entry(self,text="คำถาม", font=LARGE_FONT, width=15,textvariable=text1)
        label2.place(x=50, y=170)

        label3 = tk.Entry(self, textvariable = text2, font=LARGE_FONT,width=15,)
        label3.place(x=265,y=170)

        but  = tk.Button(self,text="เพิ่มคำศัทพ์",width=15,command=lambda :addword())
        but.place(x=200,y=230)

        text1.set("1")

        def addword():

            result = read_csv_file()
            question = []
            answer = []

            for i in result[0]:

                question.append(i)

            for j in result[1]:
                answer.append(j)

            text3 =tk.StringVar()
            input1 = str(text1.get())
            input2 = str(text2.get())

            if len(input1) !=0 or len(input2) !=0:
                if input1 not in question or input2 not in answer:

                    writer_filecsv(input1,input2)
                    print("writer file done :)")
                    text3.set("เพิ่มคำศัทพ์ สําเร็จ :)")
                    tk.Label(self,textvariable=text3,font=LARGE_FONT2).place(x=200,y=270)

                else:
                    messagebox.showerror("ผิดพลาด","คุณเพิ่มคำซ้ำ")
            else:
                messagebox.showerror("มีบางผิด","คุณลืมเพิ่ม ช่องใดช่องหนึ่งไป")

        text1.set("")
        text2.set("")

def  writer_filecsv(question, answer):

    with open("hello.csv","a",newline = '', encoding='utf-8') as csvfile:
        fi =  csv.writer(csvfile,quotechar=",",quoting=csv.QUOTE_MINIMAL)

        fi.writerow([question]+[answer])

def read_csv_file():
    question = []
    answer = []

    with open("hello.csv", encoding='utf-8',) as csvfile:
        texts  = csv.reader(csvfile, delimiter= ",")

        for row in texts:
            question.append(str(row[0]))
            answer.append(str(row[1]))

    return question, answer

# read_csv_file()

# writer_filecsv("hello","world")

app = keepit()
app.title("KEEP IT")
app.geometry("500x625")

app.mainloop()
