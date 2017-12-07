#!/usr/bin/env python

import npyscreen
from GForms import StdForm

glob = 2

def sel_changed(widget):
    mForm.sel = widget.value

class PForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.switchForm(None)

    def create(self):
        self.body = self.add(npyscreen.MultiLineEditableBoxed, values=['uyg7v8tvytviybhkbkhbhbjhbjkbjbhj','87ybybuib'], editable = False, max_height=12)
        self.ms = self.add(npyscreen.TitleSelectOne, max_height=4, value = [0,], name="Pick One",
            values = ['test4', 'test5'], scroll_exit=True)

class OForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.switchForm(None)

    def create(self):
        self.myName = self.add(npyscreen.TitleText, name='Option2 form')
        self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
        self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')
        #self.edit()

class NForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.switchForm(None)

    def create(self):
        global glob
        self.myName = self.add(npyscreen.TitleText, name=str(glob))
        self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
        self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')
        #self.edit()

class mForm(npyscreen.Form):

    nextid = 'CONFIRMFM'
    sel = 0

    def afterEditing(self):
        if int(self.sel[0]) == 0:
            self.nextid = 'OFRM'
        if int(self.sel[0]) == 1:
            self.nextid = 'PFRM'
        if int(self.sel[0]) == 2:
            self.nextid = 'TFRM2'
        self.parentApp.switchForm(self.nextid)

    def create(self):

        value_list = [
               "       -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-                                                          ",
               "     |   _   _   _   _    __  ___   _   ___  ___   _    _   _ _  |                                                        ",
               "     |  / \ | \_/ | / \  / _|| o \ / \ | __||_ _| / \  / \ | U | |                                                        ",
               "     | | o || \_/ || o |( (_ |   /| o || _|  | | | o || o ||   | |                                                        ",
               "     | |_n_||_| |_||_n_| \__||_|\\\\|_n_||_|   |_| |_n_||_n_||_n_| |                                                      ",
               "     |                                                           |                                                        ",
               "       -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-                                                          ",
               "                                                                                                                          ",
            ]

        accr_list = [
               "                                                                                                                          ",
               "                                                                                                                          ",
               "                                                                                                                          ",
               "         A.ztec/M.ayan/A.lien C.YOA R.eally                                                                               ",
               "                       A.wesome F.un T.ime A.cronyms A.re H.ard                                                           ",
               "                                                                                                                          ",
               "                                                                                                                          ",
            ]

        self.add(npyscreen.Textfield, value=value_list[0], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=value_list[1], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=value_list[2], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=value_list[3], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=value_list[4], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=value_list[5], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=value_list[6], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=value_list[7], color = 'CRITICAL', editable = False)

        self.add(npyscreen.Textfield, value=accr_list[0], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=accr_list[1], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=accr_list[2], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=accr_list[3], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=accr_list[4], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=accr_list[5], color = 'CRITICAL', editable = False)
        self.add(npyscreen.Textfield, value=accr_list[6], color = 'CRITICAL', editable = False)

        self.ms = self.add(npyscreen.TitleSelectOne, max_height=4, value = [2,], name="Pick One",
				values = ["Option1","Option2","Option3"], scroll_exit=True, value_changed_callback = sel_changed)


class TestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)

        self.registerForm('MAIN', mForm())
        self.registerForm('CONFIRMFM', NForm())
        self.registerForm('OFRM', OForm())
        self.registerForm('TFRM2', StdForm(['wrtbertbet','rbtete','yujr6u6776337'],['ch1','ch2']))
        self.registerForm('PFRM', PForm())

if __name__ == "__main__":
    App = TestApp()
    App.run()
