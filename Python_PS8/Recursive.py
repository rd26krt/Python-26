def printSumRecursive(n):
    if(n==1):
        return 1
    else:
        return n + printSumRecursive(n-1)
    
n = int(input("Enter a number"))   
sum = printSumRecursive(n)
print(f"Sum of first {n} natural numbers is {sum}")