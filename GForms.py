#!/usr/bin/env python

import npyscreen

class StdForm(npyscreen.Form):
    def __init__(self, bodytext, sellist):
        self.bodytext = bodytext
        self.sellist = sellist
        super().__init__()

    def afterEditing(self):
        self.parentApp.switchForm(None)

    def create(self):
        self.body = self.add(npyscreen.MultiLineEditableBoxed, values=self.bodytext, editable = False, max_height=18)
        self.ms = self.add(npyscreen.TitleSelectOne, max_height=4, value = [0,], name="Pick One",
            values = self.sellist, scroll_exit=True)
