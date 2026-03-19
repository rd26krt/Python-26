with open("log.html")as f:
    lines = f.readlines()

lineno =1
for line in lines:
    if "Python" in line:
        print(f"Python is present at line number : {lineno}")
    lineno += 1