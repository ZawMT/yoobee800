from person import Person
from student import Student
from staff_academic import StaffAcademic

def main():
    personn1 = Person(1, "John")
    print("Person is greeting")
    personn1.greet()

    student = Student(2, "Mary", "S1")
    print("Student is greeting")
    student.greet()
    print("Student is greeting as a Person")
    student.greet(True)

    teacher = StaffAcademic(3, "Dylan", "A1")
    print("Teacher is greeting")
    teacher.add_publication("Research on superconducting")
    teacher.greet()
    print("Teacher is greeting as a Staff")
    teacher.greet(1)
    print("Teacher is greeting as a Person")
    teacher.greet(2)

if __name__ == "__main__":
    main()