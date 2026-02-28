class Programmer:
    company = "Microsoft"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def getInfo(self):
        print(f"Name: {self.name}, Age: {self.age}, Company: {self.company}")


programmer1 = Programmer("Alice", 30)
programmer2 = Programmer("John", 25)
programmer3 = Programmer("Rohan", 35)

programmer1.getInfo()
programmer2.getInfo()
programmer3.getInfo()

