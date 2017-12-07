#!/usr/bin/env python

import npyscreen

T1D1str = '''You find yourself en route to the business district of the largest city
in Montana, Billings. In what looks to be a Lamborghini, a small bespectacled man
wearing a suit is speeding through these empty country roads at an average speed
of what looks like 100+ mph. He chuckles. "Relax" he says, "You shouldn't consider
this a kidnapping. I promise it's in the best interest of everybody. We need you
for your skills and expertise." From the backseat you see a deer walk out into the
middle of the road up ahead. "Watch out" you tell him, pointing up ahead. "Listen"
he says, "if you aren't going to relax, we're going to have problems." The car
hits the deer at a speed of about 150 miles per hour, launching it flying
straight into the air -- so much so that you couldn't see its fate on account of
it becoming too small. "Drink this" he says, "It'll help you relax". He hands you
an unopened bottle of Poland Spring water.'''

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
