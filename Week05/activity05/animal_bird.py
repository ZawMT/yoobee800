from animal import Animal

class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name) #Calling the parent's __init__
        self.feature = feature
    
    def display_info(self):
        print("I am a Bird")
        super().display_info() #Calling the parent's display_info
        print(f"My feature: {self.feature}")

class Eagle(Bird):
    def __init__(self, name, feature):
        super().__init__(name, feature)

    def display_info(self):
        return super().display_info() #Calling the parent's display_info
    
    def fly(self):
        print("I am one of the highest flyers!!!")

class Penguin(Bird):
    def __init__(self, name, feature):
        super().__init__(name, feature) #Calling the parent's __init__

    def display_info(self):
        return super().display_info() #Calling the parent's display_info
    
    def fly(self):
        print("Why fly? I prefer to walk!!!")