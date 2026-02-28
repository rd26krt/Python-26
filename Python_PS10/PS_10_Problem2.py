class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        if self.num1 > self.num2:
            return self.num1 - self.num2
        else:
            return self.num2 - self.num1
        
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero is not allowed."
        
    def square(self, num):
        return num ** 2
    
    def cube(self, num):
        return num ** 3
    
    def square_root(self, num):
        if num >= 0:
            return num ** 0.5
        else:
            return "Error: Square root of a negative number is not defined."

    @staticmethod    
    def greet():
        print("Hello! Welcome to the Calculator class.")
        
calculator = Calculator(10, 5)
calculator.greet()
print("Addition:", calculator.add())
print("Subtraction:", calculator.subtract())
print("Multiplication:", calculator.multiply())
print("Division:", calculator.divide())
print("Square of num1:", calculator.square(calculator.num1))
print("Square of num2:", calculator.square(calculator.num2))
print("Cube of num1:", calculator.cube(calculator.num1))
print("Cube of num2:", calculator.cube(calculator.num2))    
print("Square root of num1:", calculator.square_root(calculator.num1))
print("Square root of num2:", calculator.square_root(calculator.num2))