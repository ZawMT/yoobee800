from staff import Staff
from person import Person

class StaffAcademic(Staff):
    def __init__(self, id, name, staff_id):
        super().__init__(id, name, staff_id)
        self.publications = []


    def greet(self, as_a_what = 0):
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

