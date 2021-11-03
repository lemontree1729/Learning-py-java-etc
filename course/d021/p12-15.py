from tkinter import *


def clickMouse(event):  # define click event function
    global label1
    txt = ""
    if event.num == 1:
        txt += " left mouse button is clicked at ("
    elif event.num == 3:
        txt += " right mouse button is clicked at ("
    txt += str(event.x) + ", " + str(event.y) + ")"
    label1.configure(text=txt)
    label1.place(x=event.x, y=event.y)  # move label1 to coordinate where we clicked


# set-up root
window = Tk()
window.geometry("400x400")

label1 = Label(window, text="here")
window.bind("<Button>", clickMouse)
window.mainloop()
