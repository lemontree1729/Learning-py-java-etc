# import module
from tkinter import *

# declare variables
window = None
canvas = None
x1, y1, x2, y2, x3, y3 = [None] * 6


def mouseClick(self):
    global x1, y1, x2, y2, x3, y3
    x1 = self.x
    y1 = self.y
    print(x1, y1, x2, y2, x3, y3, type(self))
    # more info for print(self)


def mouseDrop(event):
    global x1, y1, x2, y2
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1 or x3, y1 or y3, x2, y2, width=5, fill="red")
    # x1 and y1 have None value
    print(x1, y1, x2, y2, x3, y3, type(event))


# What is different with <Button-1> and <ButtonPress-1>?
def mouseClick2(abcd):  # don't need to write exactly "event" as parameter
    global x1, y1, x2, y2, x3, y3
    x3 = abcd.x
    y3 = abcd.y
    print(x1, y1, x2, y2, x3, y3, type(abcd))


window = Tk()  # make root
window.title("almost paint")  # make title of Tk
# Tk class don't have to use bind
canvas = Canvas(window, height=600, width=600)
# declare Canvas with window as a master and height, width with (600, 600)
canvas.bind("<Button-1>", mouseClick)
# When <Button-1> event happends, run mouseClick(event)
# and event is instance of tkinter.Event class
# tkinter.Event class has multiple fields like x, y, delta, keys... etc
canvas.bind("<ButtonRelease-1>", mouseDrop)
canvas.bind("<ButtonPress-1>", mouseClick2)
canvas.pack()  # display canvas
window.mainloop()  # maintain loop to show interface
# code works right after tk interface closed
print(type(window))  # <class 'tkinter.Tk'>
print(type(canvas))  # <calss 'tkinter.Canvas'>
