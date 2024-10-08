from tkinter import *
from tkinter.ttk import *

class My_button:
    def __init__(self,f,b):
        self.f=Frame(f,width=500,height=600)
        self.b=Button(f,text="Click Me")
        self.f.propagate(0)
        self.f.pack()
        self.b.pack()

        self.b.bind("<Button-1>",self.button_click) 

    def button_click(self):
        print("Button Clicked")

windows=Tk()
windows.geometry("500x300")
windows.title("Button")
