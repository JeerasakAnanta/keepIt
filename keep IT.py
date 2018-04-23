import tkinter as tk
from PIL import Image,ImageTk

LARGE_FONT = ("console", 16)


class keepit(tk.Tk):

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

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo,PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("light.png")
        rende = ImageTk.PhotoImage(load)
        img = tk.Label(self,image=rende)
        img1 = tk.PhotoImage(file="light.png")
        img.image = rende
        img.pack()


        keep1 = Image.open("keep.png")
        butkeep = ImageTk.PhotoImage(keep1)

        but1 = tk.Button(self, text="จำได้",width=10 ,font=LARGE_FONT,command=lambda: controller.show_frame(PageOne))
        but1.pack(side="left",padx=10)

        but2 = tk.Button(self, text="ยังจำไม่ได้",width=10 , font=LARGE_FONT,command=lambda: controller.show_frame(PageTwo))
        but2.pack(side="left",padx=10)

        but3 = tk.Button(self, text="ทดสอบ", width=10, font=LARGE_FONT,command=lambda: controller.show_frame(PageThree))
        but3.pack(side="left",padx=10)

        but4 = tk.Button(self, text="เพิ่มคําศัพท์", width=10, font=LARGE_FONT,
                         command=lambda: controller.show_frame(PageThree))
        but4.pack(side="left", padx=10)


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
        label = tk.Label(self, text="ทดสอบ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="เพิ่มคำศัทพ์", font=LARGE_FONT)
        label.pack(pady=10, padx=10)





        button1 = tk.Button(self, text="กลับไปหน้าเเรก",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = keepit()

app.title("KEEP IT")
app.geometry("600x500")

app.mainloop()
