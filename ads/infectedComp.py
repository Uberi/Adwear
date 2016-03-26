#!/usr/bin/python

import urwid

def exit_on_q(key):
  if key in ('q', 'Q'):
    raise urwid.ExitMainLoop()

palette = [
  ('banner', 'black, bold', 'white'),
  ('streak', 'black', 'white'),
  ('bg', 'black', 'dark red'),]

header = urwid.Text(('banner', u"\n\n WARNING!!!!!!! \n SYSTEM MAY HAVE FOUND VIRUSES ON YOUR COMPUTER \n\n\n Please click below to remove the viruses. \n\n"), align='center')
map1 = urwid.AttrMap(header, 'streak')
options = []
yes = urwid.RadioButton(options, u"Eradicate Viruses")
no = urwid.RadioButton(options, u"Let Computer Die")
display_widget = urwid.GridFlow([yes, no], 15, 3, 1, 'center')
pile = urwid.Pile([map1, display_widget])
fill = urwid.Filler(pile)
map2 = urwid.AttrMap(fill, 'bg')

loop = urwid.MainLoop(
    map2,
    palette, unhandled_input=exit_on_q)

loop.set_alarm_in(10, urwid.ExitMainLoop())
loop.run()
