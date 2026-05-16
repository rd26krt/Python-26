# Magic methods
class Car:
    def __new__(cls, doors, windows, engineType):
        print("The object has started getting created")
        return super().__new__(cls)
        
    def __init__(self, doors, windows, engineType):
        self.doors = doors
        self.windows = windows
        self.engineType = engineType
    
    
    def __str__(self):
        return "The object has been initialized"
    
    def __sizeof__(self):
        print("It prints the size of the object")

    def drive(self):
        print("The person drives the car")

C = Car(4,4,"Diesel")
print(C)
C.__sizeof__()