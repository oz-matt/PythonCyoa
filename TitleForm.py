#!/usr/bin/env python

import npyscreen, sys

from TitleText import *

class TitleForm(npyscreen.ActionForm):
    def on_cancel(self):
        sys.exit()

    def afterEditing(self):
        self.parentApp.switchForm('r1t1')

    def create(self):
        for x in range(0, 7):
            self.add(npyscreen.Textfield, value=value_list[x], color = 'CRITICAL', editable = False)
        for x in range(0, 6):
            self.add(npyscreen.Textfield, value=accr_list[x], color = 'CRITICAL', editable = False)
        for x in range(0, 4):
            self.add(npyscreen.Textfield, value=sg_list[x], color = 'CRITICAL', editable = False)
        for x in range(0, 8): # Just adding more whitespace
            self.add(npyscreen.Textfield, value=sg_list[4], color = 'CRITICAL', editable = False)
