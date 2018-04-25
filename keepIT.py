#import
#============================================================================
import tkinter as tk
import csv
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

        self.tk.call('wm', 'iconphoto', self, img1) #logo

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # frames is == dic
        self.frames = {}
        # loop StartPage Page one,tow,Three and pange four

        for F in (StartPage,AddwordPage, RememberPage, unrememberPage,PageTest,Howto,EndPage):
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

        # keep1 = Image.open("keep.png")      #lode image name "keep.png"
        # butkeep = ImageTk.PhotoImage(keep1)

        but1 = tk.Button(self, text="จำได้",width=8 ,font=LARGE_FONT,
                         command=lambda: controller.show_frame(RememberPage),bg="goldenrod")
        but1.place(x=70,y=450)

        but2 = tk.Button(self, text="ยังจำไม่ได้",width=8 , font=LARGE_FONT,
                         command=lambda: controller.show_frame(unrememberPage),bg="goldenrod")
        but2.place(x=190,y=450)

        but3 = tk.Button(self, text="ทดสอบ",width=8, font=LARGE_FONT,
                         command=lambda: controller.show_frame(PageTest),bg="goldenrod")
        but3.place(x=310,y=450)

        but4 = tk.Button(self, text="เพิ่มคําศัพท์", width=8, font=LARGE_FONT,
                         command=lambda: controller.show_frame(AddwordPage),bg="goldenrod")
        but4.place(x=70,y=500)

        but5 = tk.Button(self, text="HowTo", width=8, font=LARGE_FONT,
                         command=lambda: controller.show_frame(Howto),bg="goldenrod")
        but5.place(x=190, y=500)

class RememberPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("Feame_remanber.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rende)
        img.image = rende
        img.pack()
        text1 = tk.StringVar()

        result_len = read_csv_file(filename="remember.csv")
        len_list= len(result_len[0])

        text1.set(str(len_list)+": คำ")
        t1 = tk.Label(self,textvariable= text1,font=("console", 50),justify ="center")
        t1.place(x=170,y=330)
        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage), bg="goldenrod")
        button1.place(x=370, y=550)


class unrememberPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("Feame_unmenber.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rende)
        img.image = rende
        img.pack()

        text1 = tk.StringVar()
        result_len = read_csv_file(filename="remember.csv")
        len_list = len(result_len[0])

        un_len = int(check_len("len.txt"))
        un_re =  un_len - len_list

        text1.set(str(un_re) + ": คำ")
        t1 = tk.Label(self, textvariable=text1, font=("console", 50), justify="center")
        t1.place(x=170, y=330)
        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage), bg="goldenrod")
        button1.place(x=370, y=550)

class PageTest(tk.Frame):
    def __init__(self, parent, controller,):
        tk.Frame.__init__(self, parent)
        load = Image.open("Feame_bgtest.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rende)
        img.image = rende
        img.pack()

        text1 = tk.StringVar()
        text2 = tk.StringVar()

        result  = read_csv_file(filename="word.csv")
        rember  = read_csv_file(filename="remember.csv")

        question = result[0]
        answer = result[1]
        q_rember = rember[0]
        a_menber = rember[1]

        print("rember",rember)
        print("res",result)

        btn1 = tk.Button(self, text="จำได้",font=LARGE_FONT,bg="dark green",width=6,
                         command= lambda : remember(question,answer))
        btn1.place(x=100,y=500)

        brn2 = tk.Button(self, text="เฉลย", font=LARGE_FONT, bg="Green2",width=6,
                         command=lambda : answer())
        brn2.place(x=200, y=500)

        btn3 = tk.Button(self, text="ต่อไป", font=LARGE_FONT, bg="red",width=6,
                         command=lambda : pas())
        btn3.place(x=300, y=500)

        btn_black = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage),bg="goldenrod")
        btn_black.place(x=370, y=550)

        t1 = tk.Label(self,textvariable=text1,font=LARGE_FONT3,
                      justify="center",bg="gold",width=13)
        t1.place(x=90,y=217)

        t2 = tk.Label(self, textvariable=text2, font=LARGE_FONT3,
                      justify="center",bg="gold",width=13)
        t2.place(x=90, y=330)

        count = 0
        count_len = 0

        word_question = []
        word_answer = []
        writer_filecsv_del("" ," ",filrname="wordtext.csv")
        if len(question) and len(answer) != 0:

            for i in question:
                if i not in q_rember and  i not in a_menber:

                    writer_filecsv(question[count],answer[count],filrname="word.csv")
                    count_len +=1

                count +=1

        elif len(q_rember) and len(a_menber) == 0:
            pass
        else:
            print("คุณยังไม่ได้เพิ่ม")

        test_word =read_csv_file(filename="wordtest.csv")
        word_c = test_word[0]

        print(test_word)
        word_question = test_word[0]
        word_answer = test_word[1]

        def pas():
            len_word = int(check_len("len.txt"))
            if len_word >=0:
                display_question = "A:" + str(word_question[len_word-1])
                text1.set(display_question)
                writer_len(len_word-1)
            else:
                print("done")

        def answer():
            len_answer =  int(check_len("len.txt"))
            display_answer = "A :" + word_answer[len_answer]
            text2.set(str(display_answer))

class AddwordPage(tk.Frame):       # adding word
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

        label2 = tk.Entry(self,text="คำถาม", font=LARGE_FONT, width=15,textvariable=text1,justify ="right")
        label2.place(x=50, y=170)

        label3 = tk.Entry(self, textvariable = text2, font=LARGE_FONT,width=15,justify ="right")
        label3.place(x=265,y=170)

        but  = tk.Button(self,text="เพิ่มคำศัทพ์",width=15,command=lambda :Addword())
        but.place(x=200,y=230)

        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage),bg="goldenrod")
        button1.place(x=370,y=550)

        def Addword():
            result = read_csv_file(filename="word.csv")

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

                    writer_filecsv(input1,input2,filrname="word.csv")
                    print("writer file done :)")
                    text3.set("คำถาม : "+input1+"\nคำตอบ  : "+input2+"\nเพิ่มคำศัทพ์ สําเร็จ :)")

                    tk.Label(self,textvariable=text3,font=LARGE_FONT2).place(x=128,y=270)

                    text1.set("")
                    text2.set("")

                else:
                    messagebox.showerror("ผิดพลาด","คุณเพิ่มคำซ้ำ")
            else:
                messagebox.showerror("มีบางผิด","คุณลืมเพิ่ม ช่องใดช่องหนึ่งไป")

class Howto(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("Feame_howto.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rende)
        img.image = rende
        img.pack()

        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=390, y=550)

class EndPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("Feame_end.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rende)
        img.image = rende
        img.pack()

        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=390,y=550)

def check_len(filename):
    f = open(filename,encoding='utf-8')
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

def writer_filecsv(question, answer,filrname):

    with open(filrname,"a",newline = '', encoding='utf-8') as csvfile:
        fi = csv.writer(csvfile,quotechar=",",quoting=csv.QUOTE_MINIMAL)

        fi.writerow([question]+[answer])

        csvfile.close()

def writer_filecsv_del(question, answer,filrname):

    with open(filrname,"w",newline = '', encoding='utf-8') as csvfile:
        fi = csv.writer(csvfile,quotechar=",",quoting=csv.QUOTE_MINIMAL)

        fi.writerow([question]+[answer])

        csvfile.close()
def read_csv_file(filename):
    question = []
    answer = []

    with open(filename, encoding='utf-8',) as csvfile:
        texts  = csv.reader(csvfile, delimiter= ",")

        for row in texts:

            question.append(str(row[0]))
            answer.append(str(row[1]))

    csvfile.close()
    return question, answer


app = keepit()
app.title("KEEP IT")
app.geometry("500x625")
app.mainloop()