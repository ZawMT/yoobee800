from person import Person

class Staff(Person):
    def __init__(self, staff_id):
        self.staff_id = staff_id

    def greet(self):
        print(f"Hello I am name {self.name}, I am one of the staff and my staff ID is {self.staff_id}")
