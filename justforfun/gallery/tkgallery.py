from tkinter import *
from threading import Timer
from random import randint


class Gallery:
    """
    Gallery(Widget, PhotoList, CoordinateList)

    Methods defined here:

    toggle(self, mod)
        Return before(mod=-1) or next(mod=1) photo in photolist
    relay(self, t_show, t_hide, random=False)
        Relay toggle with input showing interval and hiding interval
        if random is True, hiding time and place coordinate goes random
    stop(self)
        Stop the relay
    """

    def __init__(self, targetwidget: Widget, photolist: list, coordinatelist: list):
        self.target = targetwidget
        self.photos = photolist
        self.cords = coordinatelist
        self.x = self.cords[0][0]
        self.y = self.cords[0][1]
        self.tostop = False  # judge to stop or not
        self.isrun = False  # show relay is running now
        self.isshown = False  # show status of labTarget
        self.tognum = -1  # count toggle image number

    def toggle(self, mod: int):
        self.tognum = (self.tognum + mod) % len(self.photos)
        self.target["image"] = self.photos[self.tognum]
        if not self.isshown:
            self.target.place(x=self.x, y=self.y)
            self.isshown = True

    def relay(self, t_show: int or float, t_hide=0, random=False):
        if self.tostop:
            self.tostop = False
            return
        self.isrun = True
        if self.isshown:  # when it's showing
            self.target.place_forget()
            self.isshown = False
            if random:
                t_hide = randint(1, int(t_hide))
            Timer(t_hide, self.relay, [t_show, t_hide, random], {}).start()
        else:  # when it's not showing
            if random:
                self.x, self.y = self.cords[randint(0, len(self.photos) - 1)]
            self.toggle(1)
            Timer(t_show, self.relay, [t_show, t_hide, random], {}).start()

    def stop(self):
        self.tostop = True
        self.isrun = False
        self.target.place_forget()
        self.isshown = False


## addional coordinate search tool
def showCord(widget):
    def click(event):
        print(f"({event.x}, {event.y})")

    widget.bind("<Button-1>", click)
