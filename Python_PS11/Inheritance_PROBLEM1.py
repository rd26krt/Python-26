class TWODVECTOR:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"{self.x}i + {self.y}j")

class THREEDVECTOR(TWODVECTOR):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print(f"{self.x}i + {self.y}j + {self.z}k")

v1 = TWODVECTOR(2, 3)
v1.display() # 2 + 3
v2 = THREEDVECTOR(4, 5, 6)
v2.display() # 4 + 5 + 6    