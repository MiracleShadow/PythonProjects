from tkinter import *

#get屏幕分辨率
def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()

#get窗口分辨率
def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()

class App:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.hello = Button(frame,text='Hello',command=self.hello)
        self.hello.pack(side=LEFT)
        self.quit=Button(frame,text="Quit",fg="red",command=frame.quit)
        self.quit.pack(side=RIGHT)
    def hello(self):
        print("Hello,world")

    #在屏幕上居中显示
    def center_window(root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        print(size)
        root.geometry(size)
root=Tk()
root.title("Hello")
App.center_window(root, 300, 240)#传入初始分辨率
root.maxsize(600, 400)#设定窗口的最大分辨率
root.minsize(200,200)#设定窗口的最小分辨率
App(root)
root.mainloop()