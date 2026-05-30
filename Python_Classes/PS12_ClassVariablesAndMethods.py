# Class Variables & Methodss
class Car:
    basePrice = 100000
    def __init__(self, doors, windows, power):
        self.doors = doors
        self.windows = windows
        self.power = power
        
    
    def print_BasePrice(self):
        print ("The BasePrice is {}".format(self.basePrice))
        
    
    @classmethod
    def revise_BasePrice(cls, increment):
        cls.basePrice = cls.basePrice + (cls.basePrice * increment)/100
        
car1 = Car(4,4,2000)
print(car1.basePrice)

Car.revise_BasePrice(10)

car2 = Car(5,4,2500)
print(car2.basePrice)
