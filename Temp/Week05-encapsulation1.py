'''
Encapsulation in Python 
Source: In-class lecture
Description:
    This program is to demonstrate the basic idea of OOP encapsulation in Python
'''


class Person:
    def __init__(self, name, address, age):
        self._name = name
        self.address = address
        self.age = age

    def greet(self):
        print(f"Greeting in Person ... my name is {self._name}")


class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id

    def greet(self):
        print(f"Hi ... {self._name} here")


def main():
    student1 = Student("Alice", "Main Street 123", 20, "S1234")
    student1.greet()


if __name__ == "__main__":
    main()
