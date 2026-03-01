num = int(input("Enter a number"))

# count = 0
# for i in range(1, num+1):
#     if(num%i == 0):
#         count += 1
# if(count ==2):
#     print(f"{num} is a Prime Number")
# else:
#     print(f"{num} is not a prime number")

if(num<=1):
   print("Not Prime") 
else:

    for i in range(2, int(num**0.5)+1):
        if(num%i == 0):
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a Prime Number")