'''
Inheritance in Python
Author: Zaw Min Tun
Description:
    This program is to demonstrate the basic ideas of OOP inheritance in Python

This file is a part of a group of files:
    animal.py where the parent class is defined for animal
    animal_birds.py where the child classes for birds are defined
    animal_mamals.py where the child classes for mamals are defined
    inheritance_in_python.py which is the main file demonstrating the usage of the defined classes above
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"This is an Animal with a name {self.name}")
