# Static Methods in Pythonn
import datetime

now = datetime.datetime.now()
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
     
    @staticmethod   
    def checkYear():
        
        if now.year == 2025:
            return True
        else:
            return False
        
        
car1 = Car(4,4,2000)
print(car1.basePrice)

if(car1.checkYear()):
    pass
else:
    car1.revise_BasePrice(10)
