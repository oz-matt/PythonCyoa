#!/usr/bin/env python

import npyscreen

from StoryForm import *
from StoryText import *
from TitleForm import *

class TestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.registerForm('MAIN', TitleForm())
        self.registerForm('T1N1', StoryForm(split_str_into_list(T1N1str),['Drink water','Refuse water','Jump out of the vehicle'], ['T1N2', 'T1N2', 'T1N3']))
        self.registerForm('T1N2', StoryForm(split_str_into_list(T1N2str),['Continue asking questions','Stay silent'], ['T1N3', 'T1N3']))
        self.registerForm('T1N3', StoryForm(split_str_into_list(T1N3str),['The end :['], ['T1N3']))

if __name__ == "__main__":
    App = TestApp()
    App.run()
