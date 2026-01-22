'''
Encapsulation in Python 
Source: In-class lecture. 
Description: For the activity "Develop a python code to demonstrate whether the outputs are similar or different (see below screenshot). Explain the results have similarities or differences and why"

This file is a part of a group of two files:
    person.py where the parent class is defined for person
    student.py where the child class for student
    student.py is the main file demonstrating the inheritance nature in Python
'''


class Person:
    def __init__(self, name, address, age):
        # Protected attribute
        self._name = name

        # Public attributes
        self.address = address
        self.age = age

    # Public method
    def greet(self):
        print(f"Greeting and felicitations from maestro {self._name}")
