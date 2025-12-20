from staff import Staff

class StaffGeneral(Staff):
    def __init__(self, rate_of_pay):
        self.rate_of_pay = rate_of_pay

    def greet(self):
        print(f"Hello I am name {self.name}, I am one of the general staff and my staff ID is {self.staff_id}. I am working with this pay rate: {self.rate_of_pay}")
