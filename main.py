import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("invoice")
window.geometry("500x500")



title = Label(window, text = "Invoice")
title.grid(row = 0, column = 0, sticky = N+W)

window.mainloop()
