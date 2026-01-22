'''
Encapsulation in Python 
Source: In-class lecture. 
Description: For the activity "Develop a python code to demonstrate whether the outputs are similar or different (see below screenshot). Explain the results have similarities or differences and why"

This file is a part of a group of two files:
    person.py where the parent class is defined for person
    student.py where the child class for student
    student.py is the main file demonstrating the inheritance nature in Python
'''

from person import Person

'''
Answer: 
The outputs are similar or same as the sample name "Alice"
_name is a protected attribute of the Person class
A protected attribute can be accessed by the child class (in this case, the Student class), therefore the same information displays.
'''


class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id

    def greet(self):
        print(f"Hi {self._name}")


# Demonstratign the nature of inheritance in Python using the defined classes
student1 = Student("Alice", "123 Main Street", 20, "S1234")
student1.greet()
