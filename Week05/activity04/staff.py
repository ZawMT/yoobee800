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


from person import Person


class Staff(Person):
    def __init__(self, id, name, staff_id):
        super().__init__(id, name)
        self.staff_id = staff_id

    def greet(self):
        print(
            f"Hello I am name {self.name}, I am one of the staff and my staff ID is {self.staff_id}")


class StaffGeneral(Staff):
    def __init__(self, rate_of_pay):
        self.rate_of_pay = rate_of_pay

    def greet(self):
        print(
            f"Hello I am name {self.name}, I am one of the general staff and my staff ID is {self.staff_id}. I am working with this pay rate: {self.rate_of_pay}")


class StaffAcademic(Staff):
    def __init__(self, id, name, staff_id):
        super().__init__(id, name, staff_id)
        self.publications = []

    def greet(self, as_a_what=0):
        if as_a_what == 1:
            super().greet()
        elif as_a_what == 2:
            Person.greet(self)
        else:
            print(f"Hello I am name {self.name}, I am one of the teachers.")
            if len(self.publications) > 0:
                print(f"I published these: {self.publications}")

    def add_publication(self, publication_name):
        self.publications.append(publication_name)
