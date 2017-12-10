#!/usr/bin/env python

import npyscreen

from StoryForm import *
from StoryText import *
from TitleForm import *

class TestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.registerForm('MAIN', TitleForm())
        self.registerForm('r1t1', StoryForm(split_str_into_list(r1t1str),['Drink water','Refuse water','Jump out of the vehicle'], ['r2t1', 'r2t1', 'r2t2']))
        self.registerForm('r2t1', StoryForm(split_str_into_list(r2t1str),['Continue asking questions','Stay silent'], ['r3t1', 'r4t1']))
        self.registerForm('r2t2', StoryForm(split_str_into_list(r2t2str),['The end :['], ['EXIT']))

        self.registerForm('r3t1', StoryForm(split_str_into_list(r3t1str),['Continue'], ['r4t1']))

        self.registerForm('r4t1', StoryForm(split_str_into_list(r4t1str),['Follow him'], ['r4p5t1']))
        self.registerForm('r4p5t1', StoryForm(split_str_into_list(r4p5t1str),['Follow Dr. Hojo'], ['r4p75t1']))
        self.registerForm('r4p75t1', StoryForm(split_str_into_list(r4p75t1str),['Continue'], ['r5t1']))

        self.registerForm('r5t1', StoryForm(split_str_into_list(r5t1str),['Drink the red potion','Drink the blue potion','Drink the green potion'], ['r6t1', 'r6t2', 'r6t3']))

        self.registerForm('r6t1', StoryForm(split_str_into_list(r6t1str),['Follow the coughing man','Lay low'], ['r7t1', 'r7t2']))
        self.registerForm('r6t2', StoryForm(split_str_into_list(r6t2str),['Turn the other way','Follow the paranoid man'], ['r7t3', 'r7t4']))
        self.registerForm('r6t3', StoryForm(split_str_into_list(r6t3str),['Run out and defend Michael','Stay hidden'], ['r7t5', 'r7t6']))
        self.registerForm('r6t4', StoryForm(split_str_into_list(r6t4str),['The end :['], ['EXIT']))

        self.registerForm('r7t1', StoryForm(split_str_into_list(r7t1str),['Chase the man on Michael\'s back','Wait for a better opportunity'], ['r8t1', 'r8t2']))
        self.registerForm('r7t2', StoryForm(split_str_into_list(r7t2str),['The end :['], ['EXIT']))
        self.registerForm('r7t3', StoryForm(split_str_into_list(r7t3str),['Go for tea'], ['r8t4']))
        self.registerForm('r7t4', StoryForm(split_str_into_list(r7t4str),['Go back for Michael','Follow the man with the torch'], ['r8t5', 'r8t6']))
        self.registerForm('r7t5', StoryForm(split_str_into_list(r7t5str),['The end :['], ['EXIT']))
        self.registerForm('r7t6', StoryForm(split_str_into_list(r7t6str),['Intervene by attacking Michael\'s restrainers ','Don\'t get involved'], ['r8t7', 'r8t8']))

        self.registerForm('r8t1', StoryForm(split_str_into_list(r8t1str),['The end :['], ['EXIT']))
        self.registerForm('r8t2', StoryForm(split_str_into_list(r8t2str),['Spirulina','Michihuauhtli'], ['r9t6', 'r9t7']))
        self.registerForm('r8t4', StoryForm(split_str_into_list(r8t4str),['Alien','Robot','Human'], ['r9t3', 'r9t4', 'r9t5']))
        self.registerForm('r8t5', StoryForm(split_str_into_list(r8t5str),['Spirulina','Michihuauhtli'], ['r9t6', 'r9t8']))
        self.registerForm('r8t6', StoryForm(split_str_into_list(r8t6str),['Head back','Follow the man with the torch'], ['r7t3', 'r9t2']))
        self.registerForm('r8t7', StoryForm(split_str_into_list(r8t7str),['The end :['], ['EXIT']))
        self.registerForm('r8t8', StoryForm(split_str_into_list(r8t8str),['The end :['], ['EXIT']))

        self.registerForm('r9t1', StoryForm(split_str_into_list(r9t1str),['Go back in time->'], ['r5t1']))
        self.registerForm('r9t2', StoryForm(split_str_into_list(r9t2str),['Go back in time->'], ['r5t1']))
        self.registerForm('r9t3', StoryForm(split_str_into_list(r9t3str),['The end :['], ['EXIT']))
        self.registerForm('r9t4', StoryForm(split_str_into_list(r9t4str),['You win!'], ['EXIT']))
        self.registerForm('r9t5', StoryForm(split_str_into_list(r9t5str),['The end :['], ['EXIT']))
        self.registerForm('r9t6', StoryForm(split_str_into_list(r9t6str),['The end :['], ['EXIT']))
        self.registerForm('r9t7', StoryForm(split_str_into_list(r9t7str),['The end :['], ['EXIT']))
        self.registerForm('r9t8', StoryForm(split_str_into_list(r9t8str),['The end :['], ['EXIT']))

if __name__ == "__main__":
    App = TestApp()
    App.run()
