from PIL import Image, ImageTk
from tkinter import simpledialog
import tkinter as tk

photo = None
canvas = None


def display(image: Image.Image):
    global photo, canvas
    w, h = image.width, image.height
    window.geometry(f"{w}x{h}")
    if canvas is None:
        canvas = tk.Canvas(window, bg="#626262", bd=0, highlightthickness=0)
    canvas.delete("all")
    canvas.config(width=w, height=h)
    photo = ImageTk.PhotoImage(image=image)
    print(photo)
    canvas.create_image((w / 2, h / 2), image=photo)
    canvas.pack()


window = tk.Tk()
window.geometry("250x250")
window.title("photoshop")
image = Image.open("C:\\Users\\jm021\\Documents\\GitHub\\photo-gallery\\src\\bird.jpg")
display(image)


def setdialog(name, type: type, min=None, max=None):
    if type == int:
        f = simpledialog.askinteger
    elif type == float:
        f = simpledialog.askfloat
    if min is None and max is None:
        return f(name, f"Enter {name}")
    return f(name, f"Enter {name}({min}~{max})", minvalue=min, maxvalue=max)


def scale():
    global image
    image = image.resize((setdialog("width", int), setdialog("height", int)))
    image.show()
    display(image)
    print(photo)


print(scale.__qualname__)

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)
tool1Menu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="tool1", menu=tool1Menu)
tool1Menu.add_command(label="scale", command=scale)
window.mainloop()
