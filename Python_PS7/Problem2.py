list = ["Rohan", "Rahul", "Sammmy", "Dino", "Rajat", "Saksham"]

for i in range(1, len(list)):
    if list[i].startswith('S'):
        print(list[i])
    else:
        continue