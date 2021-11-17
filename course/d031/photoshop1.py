import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as tkfd
import tkinter.simpledialog as tksd
import tkinter.messagebox as tkms
from webbrowser import open_new  # to open usi
from collections import deque  # for temp
from math import log2

window, canvas, photo, first, last, setting = (None,) * 6


def displayImage():
    global window, canvas, photo, last
    canvas.update()
    w, h = canvas.winfo_width(), canvas.winfo_height()
    canvas.delete("all")
    photo = tk.PhotoImage()  # you should initialize photo
    photo.put(last.make_blob())  # no need to get RGB!!!!!
    canvas.create_image((w / 2, h / 2), image=photo)


def funcOpen():
    global first, last, temp, tool1List, tool2List
    temp = []
    readFp = tkfd.askopenfilename(
        filetypes=[("All image file", ".jpg .jpeg .bmp .png .tif .gif")],
    )  # PhotoImage widget supports the GIF, PGM, PPM, and PNG file formats as of Tkinter 8.6
    if readFp == "":
        return
    first = wd.Image(filename=readFp, format="png")
    last = first.clone()
    for i in tool1List:
        tool1Menu.entryconfig(i, state="active")
    for i in tool2List:
        tool2Menu.entryconfig(i, state="active")
    displayImage()


tool1List = ["scale", "resize", "flip", "flop"]
tool2List = ["rotate", "noise", "blue shift", "charcoal", "sepia_tone", "swirl"]


def funcClose():
    global canvas, tool1List, tool2List
    canvas.delete("all")
    for i in tool1List:
        tool1Menu.entryconfig(i, state="disabled")
    for i in tool2List:
        tool2Menu.entryconfig(i, state="disabled")


def funcSave():
    global last
    if last == None:
        return
    saveFp = tkfd.asksaveasfile(
        defaultextension=".png",
        filetypes=(("PNG files", ".png"), ("JPG files", ".jpg"), ("All", "*.*")),
    )
    if saveFp == None:
        return
    index = saveFp.name.rfind(".")
    last.convert(saveFp.name[index + 1 :]).save(filename=saveFp.name)


def funcReturn():
    global temp, last, fileMenu
    if len(temp) == 0:
        return
    last = temp.pop()
    displayImage()
    if len(temp) == 0:
        fileMenu.entryconfig("return", state="disabled")


def funcExit():
    global window
    window.quit()
    window.destroy()


window = tk.Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.state("zoomed")
window.title("photoshop")
window.update()

try:
    import wand.image as wd
except ModuleNotFoundError:
    tkms.showerror(
        "ModuleNotFoundError",
        "wand is not installed. To install, type 'pip install wand` in cmd",
    )
    funcExit()
except ImportError:
    yesorno = tkms.askyesnocancel(
        "ImportError", "ImageMagick is not installed. Do you want to install?"
    )
    if yesorno:
        open_new(
            r"https://download.imagemagick.org/ImageMagick/download/binaries/ImageMagick-7.1.0-13-Q16-HDRI-x64-dll.exe"
        )
    else:
        tkms.showerror("ImportError", "Install ImageMagick")
    funcExit()

###################################################


def setMsg(name, type: type, min=None, max=None):
    if type == int:
        f = tksd.askinteger
    elif type == float:
        f = tksd.askfloat
    if min == None and max == None:
        return f(name, f"Enter {name}")
    return f(name, f"Enter {name}({min}~{max})", minvalue=min, maxvalue=max)


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


def funcCfg(confname):
    global setting, last, first, temp
    tempSave(last)
    preserve = False
    data = {}
    for key, value in setting.get(confname, {}).items():
        if key == "funcname":
            funcname = value
            continue
        if type(value[0]) == tuple:
            data[key] = setMsg(key, *value[0])
            if len(value) > 1:
                preserve = True
                if len(value) == 2:
                    value.append(data[key])
                else:
                    if type(value[1]) == str:
                        data[key] = eval(
                            str(value[2]) + " " + value[1] + " " + str(data[key])
                        )
                    else:
                        data[key] = value[1](value[2], data[key])
                    value[2] = data[key]
        else:
            data[key] = value[0]
    if preserve:
        last = first.clone()
    try:
        eval("last." + funcname)(**data)
    except:
        eval("last." + funcname)(*data.values())
    displayImage()


last = wd.Image()
temp = deque([])

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

canvas = tk.Canvas(
    window,
    bg="#626262",
    bd=0,
    highlightthickness=0,
    width=window.winfo_width() * 0.85,
    height=window.winfo_height(),
)
frame = tk.Frame(
    window, width=window.winfo_width() * 0.15, height=window.winfo_height()
)
frame.place(x=window.winfo_width() * 0.85, y=0)

frameOn = False

canvas.place(x=0, y=0)
window.bind("<Control-z>", lambda event: funcReturn())

fileMenu = tk.Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="file", menu=fileMenu)
fileMenu.add_command(label="open file", command=funcOpen)
fileMenu.add_command(label="save file", command=funcSave)
fileMenu.add_command(label="return", command=funcReturn, state="disabled")
fileMenu.add_command(label="close", command=funcClose)
fileMenu.add_command(label="exit", command=funcExit)

tool1Menu = tk.Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="tool1", menu=tool1Menu)
setCfg(
    "scale",
    "resize",
    scaleX=[(float,), lambda _, x: int(x * last.width), 0],
    scaleY=[(float,), lambda _, y: int(y * last.height), 0],
)
tool1Menu.add_command(label="scale", command=lambda: funcCfg("scale"))
setCfg("resize", width=[(int,), "and"], height=[(int,), "and"])
tool1Menu.add_command(label="resize", command=lambda: funcCfg("resize"))
setCfg("flip")
tool1Menu.add_command(label="flip", command=lambda: funcCfg("flip"))
setCfg("flop")
tool1Menu.add_command(label="flop", command=lambda: funcCfg("flop"))

tool2Menu = tk.Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="tool2", menu=tool2Menu)
setCfg("rotate", degree=[(float, 0, 360), "+"])
tool2Menu.add_command(label="rotate", command=lambda: funcCfg("rotate"))
# tool2Menu.add_command(label="crop") <-------- hard to make with using funcCfg
setCfg("noise", noise_type=["laplacian"], attenuate=[(float, 0, 5)])
tool2Menu.add_command(label="noise", command=lambda: funcCfg("noise"))
setCfg("blue_shift", factor=[(float, 0, 3)])
tool2Menu.add_command(label="blue shift", command=lambda: funcCfg("blue_shift"))
setCfg("charcoal", radius=[(float,), "*"], sigma=[(float,), "*"])
tool2Menu.add_command(label="charcoal", command=lambda: funcCfg("charcoal"))
setCfg("sepia_tone", threshold=[(float,), "*"])
tool2Menu.add_command(label="sepia_tone", command=lambda: funcCfg("sepia_tone"))
setCfg("swirl", degree=[(int,), "+"])
tool2Menu.add_command(label="swirl", command=lambda: funcCfg("swirl"))
for i in tool1List:
    tool1Menu.entryconfig(i, state="disabled")
for i in tool2List:
    tool2Menu.entryconfig(i, state="disabled")


entryVar = [None] * 3
label = [None] * 3
spinbox = [None] * 3
scale = [None] * 3


def makeScale(n, foo, key):
    global frame, first, last, entryVar, label, spinbox, scale
    ###################### entryVar, label, spinbox

    def call(event):
        global first, last
        text = spinbox[n].get()
        try:
            num = int(float(text))
        except:
            try:
                num = int(float(text[:-1]))
            except:
                num = 100
        scale[n].set(log2(num / 100) * 10 + 50)
        entryVar[n].set(str(num) + "%")
        temporary = first.clone()
        temporary.resize(last.width, last.height)
        last = temporary
        arg = {key: int(eval("first." + key) * num / 100) or 1}
        eval(foo)(**arg)
        displayImage()

    def change(input):
        global first, last
        num = 2 ** ((float(input) - 50) / 10)
        entryVar[n].set(str(int(num * 100)) + "%")
        temporary = first.clone()
        temporary.resize(last.width, last.height)
        last = temporary
        arg = {key: int(eval("first." + key) * num) or 1}
        eval(foo)(**arg)
        displayImage()

    entryVar[n] = tk.StringVar(value="100%")
    label[n] = ttk.Label(frame, text=key, font=(20))
    spinbox[n] = ttk.Spinbox(
        frame,
        justify="right",
        to=6400,
        width=7,
        command=lambda: call(0),
        textvariable=entryVar[n],
    )
    spinbox[n].bind("<Return>", call)
    scale[n] = ttk.Scale(frame, length=200, to=100, value=50, command=change)
    label[n].place(x=50, y=30 + n * 60)  # x is same, y = 60 dif
    spinbox[n].place(x=170, y=30 + n * 60)
    scale[n].place(x=50, y=60 + n * 60)


makeScale(0, "last.resize", "width")
makeScale(1, "last.resize", "height")

window.mainloop()
