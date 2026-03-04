class Complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, c2):
        r = self.r + c2.r
        i = self.i + c2.i
        return Complex(r, i)
    
    def __mul__(self, c2):
        r = self.r * c2.r - self.i * c2.i
        i = self.r * c2.i + self.i * c2.r
        return Complex(r, i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    

c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(c1+c2)
print(c1*c2)
