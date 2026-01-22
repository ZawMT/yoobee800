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
from animal_birds import Eagle, Penguin
from animal_mamals import Dog, Cat


def main():
    eagle = Eagle("Eagle", "I can fly very high")
    penguin = Penguin("Penguin", "I live by the sea")
    all_animals = []
    all_animals.append(eagle)
    all_animals.append(penguin)

    # Can we see the different objects respond differently to the same method call? if yes/ no explain it in short? and what the usage of this concept?
    # Yes. Thanks to polymorphism, the corresponding function will be called for each different object
    for animal in all_animals:
        print("==============================")
        animal.display_info()
        print("And he says about flying")
        animal.fly()


if __name__ == "__main__":
    main()
