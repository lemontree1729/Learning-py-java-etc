from tkinter import *
from tkgallery import Gallery

## set root Tk
window = Tk()
window.geometry("700x700")
window.title("Photo gallery")

## set image
imgPath = "learning-py-java-etc/course/d023/src/"
imgBg = PhotoImage(file=imgPath + "space.png")
imgUseToName = [f"jeju{i}.gif" for i in range(1, 10)]
imgUseTo = [PhotoImage(file=imgPath + i) for i in imgUseToName]
imgSignName = ["arrowleft.png", "arrowright.png"]
imgSign = [PhotoImage(file=imgPath + i) for i in imgSignName]


## make main widgets and Gallery class
labBg = Label(window, image=imgBg, bd=0)
labTarget = Label(window, bg="black", image=imgUseTo[0])
gallery = Gallery(labTarget, imgUseTo, [(15, 150)])

## make sub widgets
btnLeft, btnRight = [
    Button(window, image=imgSign[i], bg="#F1E5DF", bd=0) for i in range(2)
]
btnLeft["command"] = lambda: gallery.toggle(1)
btnRight["command"] = lambda: gallery.toggle(-1)
labText = Label(window, text=imgUseToName[0], bg="#F1E5DF", font=("Ink Free", 27))

## set bind
window.bind("<Right>", lambda event: gallery.toggle(1))
window.bind("<Left>", lambda event: gallery.toggle(-1))

## set place or widgets
labBg.place(x=0, y=0)
labTarget.place(x=15, y=150)
btnLeft.place(x=150, y=4)
labText.place(x=300, y=3)
btnRight.place(x=457, y=4)

window.mainloop()
