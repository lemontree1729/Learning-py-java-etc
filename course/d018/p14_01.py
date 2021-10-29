from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("window practice")
window.geometry("600x500")
window.resizable(width=1, height=0)

label1 = Label(window, text="Python is fun!")
label2 = Label(window, text="Python is really fun!",font=30, fg="blue")
label3 = Label(window, text="Learning", bg="magenta", width=20, height=5, anchor=SE)
label1.pack()
label2.pack()
label3.pack()

imagelabel = [None]*8
image = [None]*8
for i in range(1,8):
    image[i] = PhotoImage(file=f"../gif/jeju{i}.gif")
    imagelabel[i] = Label(window, image=image[i])
# can't use imagelabel[i] = Label(window, image=PhotoImage(file=f"../gif/jeju{i}.gif"))
# why???
    if i == 1:
        imagelabel[i].config(bd=0, width=300, height=300)
    else:
        imagelabel[i].config(bd=0, width=100, height=100)

imagelabel[1].place(x=0, y=0)
imagelabel[2].pack(side=LEFT)
imagelabel[3].pack(side=LEFT)

def myFunc():
    messagebox.showinfo("button", "dog")

button1 = Button(window, text="quit", fg="red", command = quit)
button1.pack()
button2 = Button(window, image=image[4], fg="blue", command = myFunc)
button2.config(bd=0, width=50, height= 50)
button2.pack()

def myFunc2():
    if chk.get()==0:
        messagebox.showinfo("", "off")
    else:
        messagebox.showinfo("", "on")

chk = IntVar()
cb1 = Checkbutton(window, text="click it!", variable=chk, offvalue=False, command = myFunc2)
cb1.pack()

def myFunc3():
    if var.get()==1:
        label31.config(text="Python")
    elif var.get()==2:
        label31.config(text="C++")
    else:
        label31.config(text="Java")

var = IntVar()
rb1=Radiobutton(window, text="Python", variable=var, value=1, command=myFunc3)
rb2=Radiobutton(window, text="C++", variable=var, value=2, command=myFunc3)
rb3=Radiobutton(window, text="Java", variable=var, value=3, command=myFunc3)
label31 = Label(window, text="selected: ", fg="red")
rb1.pack()
rb2.pack()
rb3.pack()
label31.pack()

window.mainloop()
