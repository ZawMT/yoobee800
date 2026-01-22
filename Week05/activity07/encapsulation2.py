'''
Encapsulation in Python 
Source: In-class lecture. 
Description: For the activity "Run the attached code and explain what is the error if there is any and how we can solve it."
'''

'''
Activity result:
Running will give the following result:
Alice
123 Main St
Traceback (most recent call last):
  File "encapsulation2.py", line 73, in <module>
    print(s1.__age)
AttributeError: 'Student' object has no attribute '__age'

Answer: Not recommended, but in Python, such private member can still be accessed using the 'mangled name'.
It can be accessed as follows:
    print(s1._Person__age)
'''


class Person:
    def __init__(self, name, address, age):
        # Public attribute
        self.name = name

        # Protected attribute (subclasses can access)
        self._address = address

        # Private attribute (class-only)
        self.__age = age

    # Public method
    def greet(self):
        print(f"Hello, my name is {self.name}")

    # Public getter for private attribute
    def get_age(self):
        return self.__age


class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)

        # Private attribute (Student only)
        self.__student_id = student_id

    # Public method accessing protected attribute
    def show_address(self):
        print(f"Address: {self._address}")

    # Public getter
    def get_student_id(self):
        return self.__student_id

    # Overriding public method
    def greet(self):
        print(f"Hi, I'm {self.name} and I'm a student!")


if __name__ == "__main__":
    s1 = Student("Alice", "123 Main St", 20, "S12345")

    # Public access
    print(s1.name)

    # Protected access (allowed but discouraged outside class)
    print(s1._address)

    # Private access (will cause error)
    # print(s1.__age)
    print(s1._Person__age)

    # Correct way to access private data
    print("Age:", s1.get_age())
    print("Student ID:", s1.get_student_id())

    s1.greet()
