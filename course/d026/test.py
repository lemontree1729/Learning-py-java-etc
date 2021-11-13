from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *
from time import time

window = Tk()
window.geometry("500x500")
window.title("photoshop")

imgPath = "learning-py-java-etc/course/d026/src/"
width = 200
height = 200

with Image(filename=imgPath + "cookie1.png") as img:
    print(img.format)
    start = time()
    gifblob = img.make_blob(format="gif")
    paper1 = PhotoImage(width=width, height=height)
    paper1.put(gifblob)
    middle1 = time()
    print(middle1 - start)
    pngblob = img.make_blob(format="png")
    paper2 = PhotoImage(width=width, height=height)
    paper2.put(pngblob)
    middle2 = time()
    print(middle2 - middle1)

paper3 = PhotoImage(width=width, height=height)
a = {}
a["width"] = width
a["height"] = height
paper4 = eval("PhotoImage(width=a['width'], height=a['height'])")
label4 = Label(window, image=paper4)
label4.pack()
eval("paper3.put(pngblob)")

label1 = Label(window, image=paper1)
label2 = Label(window, image=paper2)
label1.place(x=0, y=0)
label2.place(x=200, y=200)

window.mainloop()
