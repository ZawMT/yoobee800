class Student:
    def __init__(self, name, age, student_id):
        # Attributes
        self.name = name
        self.age = age
        self.student_id = student_id

    # Method to display student details
    def display_info(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
