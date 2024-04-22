from tkinter import *
from tkinter.ttk import *

def button_click(self):
    print("Button Clicked")

windows=Tk()
windows.geometry("500x300")

f=Frame(windows,width=500,height=600) #frame creation
f.propagate(0)
f.pack()

label=Label(f,text="Hello World",
            foreground="red",
            background="yellow",)
label.pack()

button=Button(f,text="Click Me")
button.pack()

button.bind("<Button-1>",button_click)

entry=Entry(f,
            foreground="red",
            background="yellow",
            width=50)

entry.pack()
name=entry.get()





windows.mainloop()