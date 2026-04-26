class Car:
    def __init__(self, doors, windows, engineType):
        self.doors = doors
        self.windows = windows
        self.engineType = engineType

    def drive(self):
        print("The person drives the car")


class Lamborghini(Car):
    def __init__(self, doors, windows, engineType, selfDrive):
        super().__init__(doors, windows, engineType)
        self.selfDrive = selfDrive

    def ai_mode(self):
        print("Lamborghini has AI-powered controls")car1 = Lamborghini(2, 2, "V12", True)

car1.drive()
car1.ai_mode()

print(car1.selfDrive)