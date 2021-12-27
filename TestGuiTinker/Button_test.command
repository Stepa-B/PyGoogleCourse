#!/usr/local/bin/python3
import tkinter as tk
#import os

def say_hello():
    print("hello")
def add_label():
    label = tk.Label(win,text="some text")
    label.pack()
def counter ():
    global count
    count+=1
    btn4["text"] = "Number - {}".format(count)
count=0

# Directory2favicon= os.path.join(os.getcwd(),"symbol_violet.png")
# print (__file__)
win = tk.Tk()
# fav_icon=tk.PhotoImage(file=Directory2favicon)
# win.iconphoto(True, fav_icon)
win.config (bg="grey")
win.title("Хрень с кнопкой")
win.geometry("400x500+100+200")

btn1=tk.Button(win, text="Tikaii",
               command=say_hello)
btn1.pack()
btn2=tk.Button(win, text="Tikaii2",
               command=add_label)
btn2.pack()
btn4 = tk.Button(win,text="Number - {}".format(count),
                 command=counter,
                 background="yellow",
                 activebackground="blue",
                 state=tk.NORMAL # можно отключать кнопку DISABLED
                 )
btn4.pack()
win.mainloop()