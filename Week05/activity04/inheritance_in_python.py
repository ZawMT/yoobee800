from person import Person
from student import Student

def main():
    personn1 = Person(1, "John")
    print("Person is greeting")
    personn1.greet()

    student = Student(2, "Mary", "S1")
    print("Student is greeting")
    student.greet()
    print("Student is greeting as a Person")
    student.greet(True)

if __name__ == "__main__":
    main()