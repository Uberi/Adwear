#!/usr/bin/python
# -*- coding: utf-8 -*-

import urwid

palette = [
  ("banner", "black, bold", "white"),
  ("streak", "black", "white"),
  ("bg", "white", "dark red"),
]

def button_clicked(): raise urwid.ExitMainLoop()

header = urwid.Text(("banner", """

WARNING!!!!!!!
SYSTEM MAY HAVE FOUND VIRUSES ON YOUR COMPUTER

DO YOU WANT TO REPLENISH THE HARD DRIVE FLUID?

"""), align="center")
map1 = urwid.AttrMap(header, "streak")
yes1 = urwid.Button(u"YES")
yes2 = urwid.Button(u"YES")
buttons = urwid.GridFlow([yes1, yes2], 15, 3, 1, 'center')
pile = urwid.Pile([map1, buttons])
fill = urwid.Filler(pile)
map2 = urwid.AttrMap(fill, "bg")

loop = urwid.MainLoop(map2, palette)
def exit(): raise urwid.ExitMainLoop()
loop.set_alarm_in(10, exit)
loop.run()
