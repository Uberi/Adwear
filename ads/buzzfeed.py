#!/usr/bin/python
# -*- coding: utf-8 -*-

import urwid

palette = [
    ("banner", "black", "light gray"),
    ("streak", "black", "light cyan"),
    ("bg", "black", "light blue"),]

txt = urwid.Text(("banner", """

ONE WEIRD (づ｡◕‿‿◕｡)づ FRUIT THIS PERSON FOUND TO KEEP THE DOCTOR AWAY

YOU WON'T BELIEVE NUMER 5!!!

"""), align="center")
map1 = urwid.AttrMap(txt, "streak")
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, "bg")

loop = urwid.MainLoop(map2, palette)
def exit(): raise urwid.ExitMainLoop()
loop.set_alarm_in(5, exit)
loop.run()
