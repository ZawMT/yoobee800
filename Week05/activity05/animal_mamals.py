from animal import Animal

class Mamal(Animal):
    def __init__(self, name, feature):
        super().__init__(name) #Calling the parent's __init__
        self.feature = feature
    
    def display_info(self):
        super().display_info() #Calling the parent's display_info
        print(f"My feature: {self.feature}")

class Dog(Mamal):
    def __init__(self, name, feature):
        super().__init__(name, feature)

    def display_info(self):
        return super().display_info() #Calling the parent's display_info
    
    def walk(self):
        print("As a dog, I prefer to run!!!")

class Cat(Mamal):
    def __init__(self, name, feature):
        super().__init__(name, feature) #Calling the parent's __init__

    def display_info(self):
        return super().display_info() #Calling the parent's display_info
    
    def walk(self):
        print("As a cat, I prefer to jump!!!")