import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.simpledialog as tksd
import tkinter.messagebox as tkms
from webbrowser import open_new
from collections import deque


window, canvas, first, last, setting = (None,) * 5
last = wd.Image()
temp = deque([])


def displayImage():
    global window, canvas, photo, last
    w, h = last.width, last.height
    window.geometry(f"{w}x{h}")
    if not canvas:
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
    if last == wd.Image():
        return
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


def config(func, **kwargs):
    global first, last
    if last == None:
        return
    func(*kwargs.values())
    displayImage()


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

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

window.bind("<Control-z>", lambda event: funcReturn())

fileMenu = tk.Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="file", menu=fileMenu)
fileMenu.add_command(label="open file", command=funcOpen)
fileMenu.add_command(label="save file", command=funcSave)
fileMenu.add_command(label="return", command=funcReturn, state="disabled")
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
setCfg("noise", noise_type=["laplacian"], attenuate=[(float, 0, 1), "*"])
tool2Menu.add_command(label="noise", command=lambda: funcCfg("noise"))
setCfg("blue_shift", factor=[(float, 0, 1.5), "*"])
tool2Menu.add_command(label="blue shift", command=lambda: funcCfg("blue_shift"))
setCfg("charcoal", radius=[(float,), "*"], sigma=[(float,), "*"])
tool2Menu.add_command(label="charcoal", command=lambda: funcCfg("charcoal"))
setCfg("sepia_tone", threshold=[(float,), "*"])
tool2Menu.add_command(label="sepia_tone", command=lambda: funcCfg("sepia_tone"))
setCfg("swirl", degree=[(int,), "+"])
tool2Menu.add_command(label="swirl", command=lambda: funcCfg("swirl"))
setCfg("vignette", degree=[(int,), "+"])
tool2Menu.add_command(label="vignette", command=lambda: funcCfg("vignette"))
tool2Menu.add_command(label="test", command=lambda: config(last.rotate, degree=90))


window.mainloop()
