#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return super(QuestionBox, self).keypress(size, key)
        self.original_widget = urwid.Text(
            u"Nice to meet you,\n%s.\n\nPress Q to exit." %
            edit.edit_text)

edit = urwid.Edit(u"What is your name?\n")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()


# import urwid

# def question():
#     return urwid.Pile([urwid.Edit(('I say', u"What is your name?\n"))])

# def answer(name):
#     return urwid.Text(('I say', u"Nice to meet you, " + name + "\n"))

# class ConversationListBox(urwid.ListBox):
#     def __init__(self):
#         body = urwid.SimpleFocusListWalker([question()])
#         super(ConversationListBox, self).__init__(body)

#     def keypress(self, size, key):
#         key = super(ConversationListBox, self).keypress(size, key)
#         if key != 'enter':
#             return key
#         name = self.focus[0].edit_text
#         if not name:
#             raise urwid.ExitMainLoop()
#         # replace or add response
#         self.focus.contents[1:] = [(answer(name), self.focus.options())]
#         pos = self.focus_position
#         # add a new question
#         self.body.insert(pos + 1, question())
#         self.focus_position = pos + 1

# palette = [('I say', 'default,bold', 'default'),]
# urwid.MainLoop(ConversationListBox(), palette).run()

# import urwid

# choices = u'Chapman Cleese Gilliam Idle Jones Palin'.split()

# def menu(title, choices):
#     body = [urwid.Text(title), urwid.Divider()]
#     for c in choices:
#         button = urwid.Button(c)
#         urwid.connect_signal(button, 'click', item_chosen, c)
#         body.append(urwid.AttrMap(button, None, focus_map='reversed'))
#     return urwid.ListBox(urwid.SimpleFocusListWalker(body))

# def item_chosen(button, choice):
#     response = urwid.Text([u'You chose ', choice, u'\n'])
#     done = urwid.Button(u'Ok')
#     urwid.connect_signal(done, 'click', exit_program)
#     main.original_widget = urwid.Filler(urwid.Pile([response,
#         urwid.AttrMap(done, None, focus_map='reversed')]))

# def exit_program(button):
#     raise urwid.ExitMainLoop()

# main = urwid.Padding(menu(u'Pythons', choices), left=20, right=20)
# top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
#     align='center', width=('relative', 60),
#     valign='middle', height=('relative', 60),
#     min_width=20, min_height=9)
# urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()


# import urwid

# def exit_on_q(key):
#     if key in ('q', 'Q'):
#         raise urwid.ExitMainLoop()

# palette = [
#     ('banner', '', '', '', '#ffa', '#60d'),
#     ('streak', '', '', '', 'g50', '#60a'),
#     ('inside', '', '', '', 'g38', '#808'),
#     ('outside', '', '', '', 'g27', '#a06'),
#     ('bg', '', '', '', 'g7', '#d06'),]

# placeholder = urwid.SolidFill()
# loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
# loop.screen.set_terminal_properties(colors=256)
# loop.widget = urwid.AttrMap(placeholder, 'bg')
# loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

# div = urwid.Divider()
# outside = urwid.AttrMap(div, 'outside')
# inside = urwid.AttrMap(div, 'inside')
# txt = urwid.Text(('banner', u" Hello World "), align='center')
# streak = urwid.AttrMap(txt, 'streak')
# pile = loop.widget.base_widget # .base_widget skips the decorations
# for item in [outside, inside, streak, inside, outside]:
#     pile.contents.append((item, pile.options()))

# loop.run()

# import urwid

# def exit_on_q(key):
#     if key in ('q', 'Q'):
#         raise urwid.ExitMainLoop()

# palette = [
#     ('banner', 'black', 'light gray'),
#     ('streak', 'black', 'dark red'),
#     ('bg', '', ''),]

# txt = urwid.Text(('banner', u" Hello World "), align='center')
# map1 = urwid.AttrMap(txt, 'streak')
# fill = urwid.Filler(map1)
# map2 = urwid.AttrMap(fill, 'bg')
# loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
# loop.run()

# import urwid

# def question():
#     return urwid.Pile([urwid.Edit(('I say', u"What is your name?\n"))])

# def answer(name):
#     return urwid.Text(('I say', u"Nice to meet you, " + name + "\n"))

# class ConversationListBox(urwid.ListBox):
#     def __init__(self):
#         body = urwid.SimpleFocusListWalker([question()])
#         super(ConversationListBox, self).__init__(body)

#     def keypress(self, size, key):
#         key = super(ConversationListBox, self).keypress(size, key)
#         if key != 'enter':
#             return key
#         name = self.focus[0].edit_text
#         if not name:
#             raise urwid.ExitMainLoop()
#         # replace or add response
#         self.focus.contents[1:] = [(answer(name), self.focus.options())]
#         pos = self.focus_position
#         # add a new question
#         self.body.insert(pos + 1, question())
#         self.focus_position = pos + 1

# palette = [('I say', 'default,bold', 'default'),]
# urwid.MainLoop(ConversationListBox(), palette).run()




# import urwid

# palette = [('I say', 'default,bold', 'default', 'bold'),]
# ask = urwid.Edit(('I say', u"What is your name?\n"))
# reply = urwid.Text(u"")
# button = urwid.Button(u'Exit')
# div = urwid.Divider()
# pile = urwid.Pile([ask, div, reply, div, button])
# top = urwid.Filler(pile, valign='top')

# def on_ask_change(edit, new_edit_text):
#     reply.set_text(('I say', u"Nice to meet you, %s" % new_edit_text))

# def on_exit_clicked(button):
#     raise urwid.ExitMainLoop()

# urwid.connect_signal(ask, 'change', on_ask_change)
# urwid.connect_signal(button, 'click', on_exit_clicked)

# urwid.MainLoop(top, palette).run()


# import urwid

# def exit_on_q(key):
#     if key in ('q', 'Q'):
#         raise urwid.ExitMainLoop()

# class QuestionBox(urwid.Filler):
#     def keypress(self, size, key):
#         if key != 'enter':
#             return super(QuestionBox, self).keypress(size, key)
#         self.original_widget = urwid.Text(
#             u"Nice to meet you,\n%s.\n\nPress Q to exit." %
#             edit.edit_text)

# edit = urwid.Edit(u"What is your name?\n")
# fill = QuestionBox(edit)
# loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
# loop.run()

