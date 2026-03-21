with open("this.txt", "r") as f:
    content = f.read()

with open("this_copy.txt", "r") as f:
    content2 = f.read()


print(content)
print(content2)
if(content == content2):
    print("The content of both files is the same.")
else:
    print("The content of both files is different.")