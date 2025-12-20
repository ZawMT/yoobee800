from staff import Staff

class StaffAcademic(Staff):
    def __init__(self):
        self.publications = []


    def greet(self):
        print(f"Hello I am name {self.name}, I am one of the teachers. I published these: {self.publications}")

    def add_publication(self, publication_name):
        self.publications.append(publication_name)

