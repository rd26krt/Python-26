# Custom Exceptionss

class Error(Exception):
    pass
class dobException(Error):
    pass

year = int(input("Enter the Year of Birth :"))
age = 2026 - year

try:
    if(age<=30 and age>20):
        print("You are eligible for this job")
    else:
        raise dobException
except dobException:
    print("Try again for a different exam")
