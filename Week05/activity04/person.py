class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def greet(self):
        print(f"Hello I am a person with name {self.name} holding the ID {self.id}")