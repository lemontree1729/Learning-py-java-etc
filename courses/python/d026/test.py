from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *
from time import time


window.geometry("250x250")
window.title("photoshop")
mainMenu = Menu(window)
window.config(menu=mainMenu)
label = Label(window2, image=img)
fileMenu = Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="file", menu=fileMenu)

window.mainloop()
