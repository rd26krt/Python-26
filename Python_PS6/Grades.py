marks = int(input("Enter the marks of a student"))
if(marks>100 or marks<0):
    print("Invalid marks!!\nEnter the marks within the range of (0-100) only")

if(marks >=90 and marks <=100):
    print("Excellent")
elif(marks >=80 and marks<90):
    print("A Grade")
elif(marks >=70 and marks<80):
    print("B Grade")
elif(marks >=60 and marks<70):
    print("C Grade")
elif(marks >=50 and marks<60):
    print("D Grade")
elif(marks <50):
    print("Fail")