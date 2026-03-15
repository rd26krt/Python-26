n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
n3 = int(input("Enter the third number"))



def printGreatest(n1, n2, n3):
    if(n1 > n2 and n1 > n3):
        print(f"{n1} is greatest among the three nos")
    elif(n2>n3 and n2>n1):
        print(f"{n2} is greatest among the three nos")
    elif(n3>n2 and n3>n1):
        print(f"{n3} is greatest among the three nos")
    else:
        print(f"{n1}, {n2} and {n3} might be equal")

        
printGreatest(n1, n2, n3)