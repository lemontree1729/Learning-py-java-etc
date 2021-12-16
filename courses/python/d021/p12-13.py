from tkinter import *
from tkinter import messagebox


def clickImage(event):
    messagebox.showinfo("mouse", "mouse button entered")


def clickLeft(event):
    messagebox.showinfo("mouse", "left mouse button clicked")


def clickRight(event):
    messagebox.showinfo("mouse", "right mouse button clicked")


window = Tk()
window.geometry("500x500")

photo = PhotoImage(file="../../syj/python/gif/puz1.gif").zoom(5, 5)
label1 = Label(window, image=photo)
label1.bind("<Enter>", clickImage)
window.bind("<Button-1>", clickLeft)
window.bind("<Button-3>", clickRight)

label1.pack(expand=1, anchor=CENTER)
window.mainloop()
