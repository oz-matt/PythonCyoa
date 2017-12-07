#!/usr/bin/env python

import npyscreen

from StoryForm import *
from StoryText import *
from TitleForm import *

class TestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)

        self.registerForm('MAIN', TitleForm())
        self.registerForm('TFRM2', StoryForm(split_str_into_list(T1D1str),['ch1','ch2']))
        self.registerForm('TFRM1', StoryForm(split_str_into_list(T1D1str),['ch1','ch5']))

if __name__ == "__main__":
    App = TestApp()
    App.run()
