list = ["Rohan", "Subham", "Ravi", "Rohit", "Geeta", "vi"]
n = []
for i in list:
    if(not(i == "vi")):
        n.append(i.strip("vi"))

print(n)
# print(list)
# list.pop(2)
# print(list)
