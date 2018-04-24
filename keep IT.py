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
LARGE_FONT3 = ("console", 30)

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

        result = (read_csv_file())
        result1 = writer_len(len(result[0]))

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


    def __init__(self, parent, controller,):

        check = True
        tk.Frame.__init__(self, parent)
        load = Image.open("Feame_bgtest.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rende)
        img.image = rende
        img.pack()


        text1 = tk.StringVar()
        text2 = tk.StringVar()

        result  = read_csv_file()
        question = result[0]
        answer = result[1]


        label = tk.Label(self, text="ทดสอบ", font = LARGE_FONT2)
        label.pack(pady=10, padx=10)
        frame1 = tk.Frame(self)
        frame1.place(x=100, y= 100)

        btn1 = tk.Button(self, text="จำได้",font=LARGE_FONT,bg="Green2",width=6)
        btn1.place(x=100,y=465)

        brn2 = tk.Button(self, text="เฉลย", font=LARGE_FONT, bg="Green2",width=6,command=lambda : ans(question,answer))
        brn2.place(x=200, y=465)

        btn3 = tk.Button(self, text="ข้าม", font=LARGE_FONT, bg="red",width=6,command=lambda : pas(question,answer))
        btn3.place(x=300, y=465)


        btn_black = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage))
        btn_black.place(x=370, y=550)

        t1 = tk.Label(self,textvariable=text1,font=LARGE_FONT3,justify="center")
        t1.place(x=170,y=217)

        t2 = tk.Label(self, textvariable=text2, font=LARGE_FONT3, justify="center")
        t2.place(x=170, y=330)

        def pas(question ,answer):

            result_len = int(check_len())
            if result_len >=0:
                display  = str(question[result_len-1])
                text1.set(display)
                print(result_len)
                writer_len(str(result_len-1))

        def ans(question ,answer):
            result_len = int(check_len())
            if result_len >= 0:
                display = str(answer[result_len])
                text2.set(display)
                print(result_len)
                writer_len(str(result_len - 1))


class PageFour(tk.Frame):       # adding word  q

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        text1 = tk.StringVar()
        text2 = tk.StringVar()
        text3 = tk.StringVar()

        load = Image.open("Feame_bg.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rende)
        img.image = rende
        img.pack()

        label = tk.Label(self, text="เพิ่มคำศัทพ์", font=LARGE_FONT)
        label.pack()

        label2 = tk.Entry(self,text="คำถาม", font=LARGE_FONT, width=15,textvariable=text1,justify ="center")
        label2.place(x=50, y=170)

        label3 = tk.Entry(self, textvariable = text2, font=LARGE_FONT,width=15,justify ="center")
        label3.place(x=265,y=170)

        but  = tk.Button(self,text="เพิ่มคำศัทพ์",width=15,command=lambda :addword())
        but.place(x=200,y=230)

        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=370,y=550)

        def addword():

            result = read_csv_file()
            question = []
            answer = []

            for i in result[0]:

                question.append(i)

            for j in result[1]:
                answer.append(j)

            input1 = str(text1.get())
            input2 = str(text2.get())

            if len(input1) !=0 and len(input2) !=0:

                if input1 not in question or input2 not in answer:

                    writer_filecsv(input1,input2)
                    print("writer file done :)")
                    text3.set("คำถาม : "+input1+"\nคำตอบ  : "+input2+"\nเพิ่มคำศัทพ์ สําเร็จ :)")

                    tk.Label(self,textvariable=text3,font=LARGE_FONT2).place(x=128,y=270)

                    text1.set("")
                    text2.set("")

                else:
                    messagebox.showerror("ผิดพลาด","คุณเพิ่มคำซ้ำ")
            else:
                messagebox.showerror("มีบางผิด","คุณลืมเพิ่ม ช่องใดช่องหนึ่งไป")

def check_len():
    f = open("len.txt",encoding='utf-8')
    check = f.read()
    f.close()
    return check

def  writer_len(number):
    f = open('len.txt', 'w', encoding='utf-8',)
    f.write(str(number))
    f.close()

def writer_filetext(name_file):
    f = open('helloworld.txt', 'a',encoding='utf-8',newline='')
    f.write('hello world\n')
    f.close()

def  writer_filecsv(question, answer):

    with open("hello.csv","a",newline = '', encoding='utf-8') as csvfile:
        fi =  csv.writer(csvfile,quotechar=",",quoting=csv.QUOTE_MINIMAL)

        fi.writerow([question]+[answer])

        csvfile.close()

def read_csv_file():
    question = []
    answer = []

    with open("hello.csv", encoding='utf-8',) as csvfile:
        texts  = csv.reader(csvfile, delimiter= ",")

        for row in texts:
            question.append(str(row[0]))
            answer.append(str(row[1]))

    writer_len(len(question))

    csvfile.close()

    return question, answer

app = keepit()
app.title("KEEP IT")
app.geometry("500x625")

app.mainloop()


