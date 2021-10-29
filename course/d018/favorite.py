from tkinter import *


# making root
window = Tk()
window.title("window practice")
window.geometry("660x440")

# making background image with Label class
bgimage = PhotoImage(file=f"../gif/jeju1.gif")
bglabel = Label(window, image=bgimage, bd = 0)
bglabel.place(x=0, y=0) # use place to float

# making header with Label class
favlabel = Label(window, text="YOUR FAVORITE ANIMAL!", font=("Times", "30"),fg="blue", bg="green")
favlabel.pack(pady = 10)

rbvar = IntVar() # defining int variable used in tkinter
#rbvar.set(0) # set default value as 0

# variable declare
images = [None]*3
rb = [None]*3
favlist = ("cat", "dog", "horse")

def myFunc(): # command function(act when button activates)
    global images, favlist, cnt
    for i in range(3):
        if i == rbvar.get():
            label1.config(image=images[i])
            label2.config(text=f"Do you like this {favlist[i]}?")
            break
        
for i in range(3):
    # making 3 image addresses
    images[i] = PhotoImage(file=f"../gif/{favlist[i]}.png")
    # making 3 radiobutton 
    rb[i] = Radiobutton(window, text=favlist[i], variable=rbvar, value=i, command=myFunc)
    rb[i].pack(pady=10)

# making 2 labels
label1 = Label(window, image=images[0], bg="black")
label1.pack(pady=5)
label2 = Label(window, text="select the image")
label2.pack()

window.mainloop() # delaying program end
