from tkinter import *
from tkinter import messagebox
from tkgallery import Gallery


## set root Tk
window = Tk()
window.geometry("700x700")
window.title("cookies!")

## set image
imgPath = "learning-py-java-etc/justforfun/gallery/src/"
imgUseTo = [PhotoImage(file=imgPath + f"cookie{i}.png") for i in range(7)]
imgSignName = ["left.png", "right.png", "start.png", "end.png", "fast.png"]
imgSign = [PhotoImage(file=imgPath + i) for i in imgSignName]
imgBg = PhotoImage(file=imgPath + "space.png")

## set global variables
crds = [(171, 27), (485, 19), (136, 235), (562, 196), (19, 429), (327, 599), (602, 608)]
hit = 0
miss = 0


def resultSet(target, hit, miss):
    score = (hit * 2 - miss) * 10
    if score < -99 or score > 999:
        target["text"] = f"Score:\n{score}\nHit:{hit}\nMiss:{miss}"
    else:
        target["text"] = f"Score:{score}\nHit:{hit}\nMiss:{miss}"


def clickHit(event):
    global labText, hit, miss
    hit += 1
    resultSet(labText, hit, miss)


def clickMiss(event):
    global labText, hit, miss
    miss += 1
    resultSet(labText, hit, miss)


def clickStop(gallery):
    global labText, hit, miss
    gallery.stop()
    messagebox.showinfo("game ended", f"your score is {(hit*2- miss)*10}")
    hit, miss = 0, 0
    resultSet(labText, 0, 0)


## make main widgets and Gallery class
labBg = Label(window, image=imgBg, bd=0)
labTarget = Label(window, bg="#F1E5DF", bd=0, cursor="star")
cookie = Gallery(labTarget, imgUseTo, crds)

## make sub widgets
btnPrev, btnNext, btnSlow, btnStop, btnFast = [
    Button(window, image=imgSign[i], bg="#F1E5DF", bd=0) for i in range(5)
]
btnPrev["command"] = lambda: cookie.toggle(1)
btnNext["command"] = lambda: cookie.toggle(-1)
btnSlow["command"] = lambda: None if cookie.isrun else cookie.relay(1, 2, True)
btnFast["command"] = lambda: None if cookie.isrun else cookie.relay(0.5, 5, True)
btnStop["command"] = lambda: clickStop(cookie)
labText = Label(window, bg="#F1E5DF", bd=0, font=("Ink Free", 25), justify="left")
resultSet(labText, 0, 0)

## set bind
labBg.bind("<Button-1>", lambda event: clickMiss(event) if cookie.isrun else None)
labTarget.bind("<Button-1>", lambda event: clickHit(event) if cookie.isrun else None)

## set place of widgets
labBg.place(x=0, y=0)
btnPrev.place(x=367, y=9)
btnSlow.place(x=455, y=100)
btnStop.place(x=541, y=132)
btnNext.place(x=635, y=163)
btnFast.place(x=579, y=89)
labText.place(x=0, y=0)

window.mainloop()
