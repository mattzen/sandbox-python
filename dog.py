class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.breed = "owaczarek"
    
    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")