import tkinter as tk

win = tk.Tk()
win.config (bg="#e6f2ff")
win.title("Хреногрид}")
win.geometry("500x600+300+300")

btn1 = tk.Button(win, text= "hello 1efawfwaefwefaswew")
btn2 = tk.Button(win, text= "hello 2fwefawef")
btn3 = tk.Button(win, text= "hello 3")
btn4 = tk.Button(win, text= "hello 4faweefawef")
btn5 = tk.Button(win, text= "hello 5wefawef")
btn6 = tk.Button(win, text= "hello 6ewfawef")
btn7 = tk.Button(win, text= "hello 7")
btn8 = tk.Button(win, text= "hello 8fewa")

btn1.grid( row = 0, column = 0, stick="e")
btn2.grid( row = 0, column = 1, stick="e")
btn3.grid( row = 1, column = 0, stick="e")
btn4.grid( row = 1, column = 1, stick="e")
btn5.grid( row = 2, column = 0, stick="e")
btn6.grid( row = 2, column = 1, stick="e")
btn7.grid( row = 3, column = 0, stick="e")
btn8.grid( row = 3, column = 1, stick="e")

win.grid_columnconfigure(0,minsize = 200)
win.grid_columnconfigure(0,minsize = 200)

win.mainloop()