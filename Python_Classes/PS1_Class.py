class Car:
    def __init__(self, door, window, enginetype):
        self.doors = door
        self.windows = window
        self.enginetype = enginetype
        
    def self_driving(self):
        print ("This is a {} car".format(self.enginetype))
        
        
Car1 = Car(4,4,"Petrol")
print(Car1.doors)
print(Car1.windows)
Car1.self_driving()


Car2 = Car(5,4,"Diesel")
print(Car2.doors)
print(Car2.windows)
Car2.self_driving()