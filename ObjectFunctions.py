#!/usr/bin/python

#!Object Functions

class Pupil:
    def __init__(self, name, grade, age, marks):
        self.name = name
        self.grade = grade
        self.age = age
        self.marks = marks

    def on_honor_roll(self):
        if self.marks >= 350:
            return True
        else:
            return False

pupil1 = Pupil("Nefatiti", 6, 11, 401)
pupil2 = Pupil("Seth", 12, 17, 295)

print(pupil1.on_honor_roll())


#!Go Ahead and test it out!!!!
