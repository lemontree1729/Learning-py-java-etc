from tkinter import *

## define function of before and next
def toggle(mod: int):
    global num, labUseTo, imgUseTo
    num = (num + mod) % len(imgUseTo)
    labUseTo["image"] = imgUseTo[num]
    labText["text"] = imgUseToName[num]


## global number setting
cnt = 0
num = 0

## root setting
window = Tk()
window.geometry("700x700")
window.title("image gallery")

## image setting
imgPath = "learning-py-java-etc/course/d023/src/"
imgUseToName = [f"jeju{i}.gif" for i in range(1, 10)]
imgUseTo = [PhotoImage(file=imgPath + i) for i in imgUseToName]
imgBg = PhotoImage(file=imgPath + "space.png")
imgLeft = PhotoImage(file=imgPath + "arrowleft.png")
imgRight = PhotoImage(file=imgPath + "arrowright.png")

## bind setting
window.bind("<Prior>", lambda event: toggle(1))
window.bind("<Right>", lambda event: toggle(1))
window.bind("<Next>", lambda event: toggle(-1))
window.bind("<Left>", lambda event: toggle(-1))

## widget setting
labBg = Label(window, image=imgBg, bd=0)
btnLeft = Button(window, image=imgLeft, bg="#F1E5DF", bd=0, command=lambda: toggle(1))
btnRight = Button(
    window, image=imgRight, bg="#F1E5DF", bd=0, command=lambda: toggle(-1)
)
labUseTo = Label(window, image=imgUseTo[0])  # initial image to show
labText = Label(window, text=imgUseToName[0], bg="#F1E5DF", font=("Curlz MT", 27))

## place widgets
labBg.place(x=0, y=0)
btnLeft.place(x=150, y=4)
labText.place(x=304, y=-2)
btnRight.place(x=457, y=4)
labUseTo.place(x=15, y=150)

window.mainloop()
