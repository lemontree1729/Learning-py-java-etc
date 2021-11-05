from tkinter import *
from tkinter import messagebox
from threading import Timer
from random import randint

## global number setting
tostop = False
isshown = True
hit = 0
miss = 0
num = -1

## toggle before and after
def doToggle(mod: int):
    global num, labUseTo, imgUseTo
    num = (num + mod) % len(imgUseTo)
    labUseTo["image"] = imgUseTo[num]


def doRelay():
    global tostop
    if tostop:
        tostop = False
        return
    doToggle(1)
    x0, y0 = cord[randint(0, 6)]
    labUseTo.place(x=x0, y=y0)
    Timer(1.0, doRelay).start()


def doFast():
    global tostop, isshown
    if tostop:
        tostop = False
        return
    isshown = not isshown
    if not isshown:
        doToggle(1)
        x0, y0 = cord[randint(0, 6)]
        labUseTo.place(x=x0, y=y0)
        Timer(0.5, doFast).start()
    else:
        labUseTo.place_forget()
        Timer(randint(1, 5), doFast).start()


def doStop():
    global tostop, hit, miss
    tostop = True
    messagebox.showinfo("game ended", f"total score: {hit*2- miss}")
    hit = 0
    miss = 0


def clickCookie():
    global hit
    hit += 1
    labText["text"] = f"Score: {hit*2- miss} Hit: {hit} Miss: {miss}"


def missClick():
    global miss
    miss += 1
    labText["text"] = f"Score: {hit*2- miss} Hit: {hit} Miss: {miss}"


## root setting
window = Tk()
window.geometry("700x700")
window.title("cookies!")

## image setting
imgPath = "learning-py-java-etc/course/d023/src/"
imgUseTo = [PhotoImage(file=imgPath + f"puz{i}.png") for i in range(7)]
imgSignName = ["left.png", "right.png", "start.png", "end.png", "fast.png"]
imgSign = [PhotoImage(file=imgPath + i) for i in imgSignName]
imgBg = PhotoImage(file=imgPath + "space.png")
## coordinate setting
cord = [(171, 27), (485, 19), (136, 235), (562, 196), (19, 429), (327, 599), (602, 608)]

## widget making
labBg = Label(window, image=imgBg, bd=0)
btnPrev = Button(
    window, image=imgSign[0], bg="#F1E5DF", bd=0, command=lambda: doToggle(1)
)
btnNext = Button(
    window, image=imgSign[1], bg="#F1E5DF", bd=0, command=lambda: doToggle(-1)
)
btnStart = Button(window, image=imgSign[2], bg="#F1E5DF", bd=0, command=doRelay)
btnStop = Button(window, image=imgSign[3], bg="#F1E5DF", bd=0, command=doStop)
btnFast = Button(window, image=imgSign[4], bg="#F1E5DF", bd=0, command=doFast)
labUseTo = Label(window, bg="#F1E5DF", bd=0, cursor="star red")
labText = Label(
    window,
    bg="#F1E5DF",
    bd=0,
    text="Score: 0 Hit: 0 Miss: 0",
    font=("Curlz MT", 28),
    wraplength=150,
)

## bind setting
window.bind("<Right>", lambda event: doToggle(1))
window.bind("<Left>", lambda event: doToggle(-1))
labUseTo.bind("<Button-1>", lambda event: clickCookie())


## plcae widgets
labBg.place(x=0, y=0)
btnPrev.place(x=367, y=9)
btnStart.place(x=455, y=100)
btnStop.place(x=541, y=132)
btnNext.place(x=635, y=163)
btnFast.place(x=579, y=89)
labUseTo.place(x=171, y=27)
labText.place(x=0, y=0)

window.mainloop()
