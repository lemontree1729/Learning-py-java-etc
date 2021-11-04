from tkinter import *
import sys


window = Tk()
window.geometry("700x700")

frame1 = Frame(window, relief="solid", width=500, height=500, bd=2)
frame1.pack()
chesslb = [[0] * 8 for _ in range(8)]
img = [[0] * 8 for _ in range(2)]
bkimg = PhotoImage(file="chimg/bk.png")
blankimg = PhotoImage(file="chimg/blank.png")
bkdotimg = PhotoImage(file="chimg/bkdot.png")
bkimg = bkimg.zoom(5, 5)
for x in range(8):
    for y in range(8):
        chesslb[y][x] = Button(frame1, bd=0, text="●", font=("verdana"), fg="purple")
        if (x + y) % 2:
            chesslb[y][x].config(bg="#d08c4a")
        else:
            chesslb[y][x].config(bg="#facb9c", image=bkimg, compound="c")
        chesslb[y][x].grid(column=x + 1, row=y + 1, sticky="nesw")


print(chesslb[0][0].config())
print(sys.getsizeof(bkimg))
bkimg.name = "bkimg"
print(bkimg.name)
matchimg = {bkimg.name: bkimg}
print(matchimg)

window.mainloop()
