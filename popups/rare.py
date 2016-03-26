#!/usr/bin/python
# -*- coding: utf-8 -*-

import urwid

palette = [
  ("banner", "black, bold", "white"),
  ("streak", "black", "white"),
  ("bg", "white", "dark green"),
]

def button_clicked(): raise urwid.ExitMainLoop()

header = urwid.Text(("banner", r"""

RARE-PEPE-AUCTIONS.COM

AUCTION CLEARINGHOUSE FOR THE RAREST OF PEPES

CERTIFIED GENUINE BY /r/uwaterloo

          _...._
       .()      '() 
      /:  \-""-./  \
     /:' / \    \   \
    |:' |     ^ /'-._|
    |:' |  ,_ ,'_.---;`
     \:.\    ';`    /
      \:.\    \    /
  jgs  '-:\____\.-'

"""), align="left")
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
