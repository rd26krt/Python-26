def even_odd(num):
    if(num%2 ==0):
        print("{} is a even number".format(num))
    else:
        print("{} is a odd number".format(num))


l1 =[1,2,3,78,85.46,98,32,68,72,96]

print(list(map(even_odd,l1)))