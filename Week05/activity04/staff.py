from person import Person

class Staff(Person):
    def __init__(self, id, name, staff_id):
        super().__init__(id, name)
        self.staff_id = staff_id

    def greet(self):
        print(f"Hello I am name {self.name}, I am one of the staff and my staff ID is {self.staff_id}")
