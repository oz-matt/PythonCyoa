#!/usr/bin/env python

import npyscreen, sys

def split_str_into_list(str):
    buff = str
    L = []
    while len(buff) > 75:
        idx = 75
        while buff[idx-2] != ' ':
            idx = idx-1

        L.append(buff[:idx-1])
        buff = buff[idx-1:]
    L.append(buff)
    return L

class StoryForm(npyscreen.Form):

    sel = 0

    def __init__(self, bodytext, sellist, nextformidlist):
        self.bodytext = bodytext
        self.sellist = sellist
        self.nextformidlist = nextformidlist
        super().__init__()

    def sel_changed(self, widget):
        self.sel = widget.value

    def afterEditing(self):
        nextformid = self.nextformidlist[int(self.sel[0])]
        print(nextformid)
        if nextformid == 'EXIT':
            sys.exit()
        self.parentApp.switchForm(nextformid)

    def create(self):
        self.body = self.add(npyscreen.MultiLineEditableBoxed, values=self.bodytext, editable = False, max_height=18)
        self.ms = self.add(npyscreen.TitleSelectOne, max_height=4, value = [0,], name="Choose One", value_changed_callback = self.sel_changed,
            values = self.sellist, scroll_exit=True)
