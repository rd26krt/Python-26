def Outer(func):
    x = 10
    
    def inner():
        print(2*x)
        func()
        
    return inner    
        


@Outer
def printName():
    print("ABC is my name")
    
printName()


# A decorator is a function that wraps another function to extend or modify its behavior without changing its code.