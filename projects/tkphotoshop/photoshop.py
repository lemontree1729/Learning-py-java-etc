import tkinter as tk
from tkinter import Event, Variable, Widget, ttk
import tkinter.filedialog as tkfd
import tkinter.simpledialog as tksd
import tkinter.messagebox as tkms
from webbrowser import open_new
from collections import deque


def displayImage():
    global window, canvas, photo, last
    w, h = last.width, last.height
    window.geometry(f"{w}x{h}")
    if canvas == None:
        canvas = tk.Canvas(window, bg="#626262", bd=0, highlightthickness=0)
    canvas.delete("all")
    canvas.config(width=w, height=h)
    photo = tk.PhotoImage()  # you should initialize photo
    photo.put(last.make_blob())  # no need to get RGB!!!!!
    canvas.create_image((w / 2, h / 2), image=photo)
    canvas.pack()


def funcOpen():
    global first, last, temp
    temp = []
    readFp = tkfd.askopenfilename(
        filetypes=[("All image file", ".jpg .jpeg .bmp .png .tif .gif")],
    )  # PhotoImage widget supports the GIF, PGM, PPM, and PNG file formats as of Tkinter 8.6
    if readFp == "":
        return
    first = wd.Image(filename=readFp, format="png")
    last = first.clone()
    displayImage()


def funcSave():
    global last
    if last == None:
        return
    saveFp = tkfd.asksaveasfile(
        defaultextension=".png",
        filetypes=(("PNG files", ".png"), ("All", "*.*")),
    )
    if saveFp == None:
        return
    last.convert("png").save(filename=saveFp.name)


def funcExit():
    global window
    window.quit()
    window.destroy()


window, canvas, first, last, photo, setting = (None,) * 6

window = tk.Tk()
window.geometry("250x250")
window.title("photoshop")

try:
    import wand.image as wd
except ModuleNotFoundError:
    tkms.showerror(
        "ModuleNotFoundError",
        "wand is not installed. To install, type 'pip install wand` in cmd",
    )
    funcExit()
except ImportError:
    yesorno = tkms.askyesnocancel("ImportError", "ImageMagick is not installed. Do you want to install?")
    if yesorno:
        open_new(
            r"https://download.imagemagick.org/ImageMagick/download/binaries/ImageMagick-7.1.0-13-Q16-HDRI-x64-dll.exe"
        )
    else:
        tkms.showerror("ImportError", "Install ImageMagick")
    funcExit()

############################################################

last = wd.Image()
temp = deque([])

msgi = tksd.askinteger
msgf = tksd.askfloat


def funcReturn():
    global temp, last, fileMenu
    if len(temp) == 0:
        return
    last = temp.pop()
    displayImage()
    if len(temp) == 0:
        fileMenu.entryconfig("return", state="disabled")


def setCfg(confname, funcname=None, **kwargs):
    global setting
    kwargs["funcname"] = funcname or confname
    if setting == None:
        setting = dict()
    if setting.get(confname, None) == None:
        setting[confname] = kwargs
    else:
        for key in kwargs:
            setting[confname][key] = kwargs[key]


def tempSave(last):
    global temp, fileMenu
    if len(temp) < 10:
        temp.append(last.clone())
    else:
        temp.popleft()
        temp.append(last.clone())
    fileMenu.entryconfig("return", state="normal")


def config(func, **kwargs):
    global first, last
    if last == None:
        return
    func(*kwargs.values())
    displayImage()


mainMenu = tk.Menu(window)
window["menu"] = mainMenu

window.bind("<Control-z>", lambda event: funcReturn())

fileMenu = tk.Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="file", menu=fileMenu)
fileMenu.add_command(label="open file", command=funcOpen)
fileMenu.add_command(label="save file", command=funcSave)
fileMenu.add_command(label="return", command=funcReturn, state="disabled")
fileMenu.add_command(label="exit", command=funcExit)

tool1Menu = tk.Menu(mainMenu, tearoff="off")
tool2Menu = tk.Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="tool2", menu=tool2Menu)
tool2Menu.add_command(label="test", command=lambda: config(last.rotate, degree=90))

hi = tk.IntVar()
hey = tk.StringVar()


def sett():
    print(hey.get())


a = ttk.Spinbox(window, to=20, textvariable=hey, command=sett, validate="key", validatecommand=sett)
hi.set(15)
hey.set(15)
print(hey)
a.pack()
b = tk.LabelFrame(window)
b.pack()
scale = ttk.Scale(window, orient="horizontal", to_=100, length=300)
scale.pack()


class ToggleBar:
    def __init__(self, root, text, from_, to, value):
        self.frame = tk.Frame(root)
        self.var = tk.DoubleVar()
        self.label = tk.Label(self.frame, text=text, textvariable=1)
        self.spin = ttk.Spinbox(
            self.frame,
        )
        self.scale = ttk.Scale(
            self.frame,
            from_=from_,
            to=to,
            value=value,
            orient="horizontal",
        )

    def match(self):
        pass

    def get(self):
        self.scale.get()

    def set(self):
        self.scale.set()


window.mainloop()
