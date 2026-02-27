marks1  = int(input("Enter the first subject marks"))
marks2  = int(input("Enter the second subject marks"))
marks3  = int(input("Enter the third subject marks"))
if(marks1>100 or marks1< 0 or marks2>100 or marks2 < 0 or marks3 >100 or marks3<0):
    print("Enter a valid marks within the range of 0 to 100")
else:
    avg = (marks1 + marks2 + marks3)/3

    if(avg >=40 and marks1 >=33 and marks2 >=33 and marks3>=33):
        print("You are passed", avg)
    else:
        print("You are failed")