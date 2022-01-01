#!/usr/local/bin/python3

import tkinter as tk

win = tk.Tk()
fav_icon=tk.PhotoImage(file="symbol_violet.png")
win.iconphoto(True, fav_icon)
win.config (bg="#e6f2ff")
win.title("ЭХренотень")
win.geometry("300x400+300+300")

label_1 = tk.Label( win, text="Privet", #text area
                    bg="#0066cc", #цвет подложки
                    fg="red", #цвет текста
                    font= ("calibri",18,"bold"), # шрифт кортежем
                    padx=10, # поля вокруг текста по иксу
                    pady=5, # поля по У
                    width= 10, # ширина поля в знаках
                    height=2, # высота поля в знаках
                    relief= tk.RAISED, #  границы
                    justify= tk.LEFT  # выравнивание текста 
                    )
label_1.pack()

win.mainloop()
