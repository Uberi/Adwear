#!/usr/bin/python
# -*- coding: utf-8 -*-

import urwid

palette = [
  ("banner", "black, bold", "white"),
  ("streak", "black", "white"),
  ("bg", "white", "dark green"),
]

def button_clicked(): raise urwid.ExitMainLoop()

header = urwid.Text(("banner", """

SINGLE PROCESSES AROUND YOU IN LOW EARTH ORBIT!!!!!

"""), align="center")
map1 = urwid.AttrMap(header, "streak")
yes1 = urwid.Button(u"DISMISS")
yes2 = urwid.Button(u"CANCEL")
yes3 = urwid.Button(u"NO")
buttons = urwid.GridFlow([yes1, yes2, yes3], 8, 3, 1, "center")
pile = urwid.Pile([map1, buttons])
fill = urwid.Filler(pile)
map2 = urwid.AttrMap(fill, "bg")

loop = urwid.MainLoop(map2, palette)
def exit(): raise urwid.ExitMainLoop()
loop.set_alarm_in(10, exit)
loop.run()
