class Train:

    def __init__(self, name, age, trainNumber):
        self.name = name
        self.age = age
        self.trainNumber = trainNumber

    def bookTicket(self):
        if self.age < 5:
            print(f"Sorry {self.name}, you are not eligible to book a ticket.")
        else:
            print(f"Congratulations {self.name}, your ticket has been booked successfully!")

    def getStatus(self):
        print(f"The status of train number {self.trainNumber} is on time.")

    def trainInfo(self):
        print(f"Train number {self.trainNumber} is a superfast express train and runs between City A and City B.")
        print("It has 20 coaches and offers various amenities for passengers.")

train = Train("Alice", 4, 12345)
train.bookTicket()
train.getStatus()
train.trainInfo()
print("--"*20)
train1 = Train("Sam", 4, 97436)
train1.bookTicket()
train1.getStatus()
train1.trainInfo()
train1.trainInfo()