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

from animal import Animal


class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name)  # Calling the parent's __init__
        self.feature = feature

    def display_info(self):
        print("I am a Bird")
        super().display_info()  # Calling the parent's display_info
        print(f"My feature: {self.feature}")


class Eagle(Bird):
    def __init__(self, name, feature):
        super().__init__(name, feature)

    def display_info(self):
        return super().display_info()  # Calling the parent's display_info

    def fly(self):
        print("I am one of the highest flyers!!!")


class Penguin(Bird):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Calling the parent's __init__

    def display_info(self):
        return super().display_info()  # Calling the parent's display_info

    def fly(self):
        print("Why fly? I prefer to walk!!!")
