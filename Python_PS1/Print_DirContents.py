import os

# Path of the directory
path = "."   # current directory

# List directory contents
contents = os.listdir(path)

for item in contents:
    print(item)
