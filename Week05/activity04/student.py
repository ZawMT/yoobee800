from person import Person

class Student(Person):
    def __init__(self, id, name, student_id):
        super().__init__(id, name)
        self.student_id = student_id

    def greet(self, as_a_person = False):
        if as_a_person:
            super().greet()
        else:    
            print(f"Hello I am a student with name {self.name} and my student ID is {self.student_id}")