a=10
b=0
c=15

try:
    print(a/b)
except ZeroDivisionError:
    print("Please!! Donot divide a number by zero \n Give a number greater than zero")
   
print("Value of C is {}".format(c))