def Outer():
    x = 10
    
    def inner():
        print(2*x)
        
    return inner    
        
f=Outer()
f()

# A closure is a function that captures variables from its enclosing scope and can use them even after the outer function has finished execution.