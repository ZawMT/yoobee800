'''
Inheritance in Python
Author: Zaw Min Tun
Description:
    This program is to demonstrate the basic ideas of OOP inheritance in Python

This file is a part of a group of files:
    person.py where the parent class is defined for person
    staff.py where the child classes for staff are defined
    student.py where the child class for student is defined
    inheritance_in_python.py which is the main file demonstrating the usage of the defined classes above
'''


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def greet(self):
        print(
            f"Hello I am a person with name {self.name} holding the ID {self.id}")
