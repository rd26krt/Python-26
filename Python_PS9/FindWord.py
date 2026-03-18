with open("log.html") as f:
    content = f.read()
    if "Python" in content:
        print("Python is present")
    else:
        print("Python is not present")
