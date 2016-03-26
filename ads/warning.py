#!/usr/bin/python
# -*- coding: utf-8 -*-

import urwid

palette = [
    ("banner", "black", "light gray"),
    ("streak", "black", "dark green"),
    ("bg", "black", "dark magenta"),]

txt = urwid.Text(("banner", """

GET NORTON 420 TODAY FOR ADVANCED PC PROTECTION!!!!!

> GET A FREE 30 SECOND TRIAL <

"""), align="center")
map1 = urwid.AttrMap(txt, "streak")
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, "bg")

loop = urwid.MainLoop(map2, palette)
def exit(): raise urwid.ExitMainLoop()
loop.set_alarm_in(5, exit)
loop.run()
