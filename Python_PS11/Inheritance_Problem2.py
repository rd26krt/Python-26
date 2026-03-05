class Animals:
    pass

class Pet(Animals):
    pass

class Dog(Pet):

    @staticmethod
    def bark():
        print("Woof!")

d1 = Dog()
d1.bark() # Woof!