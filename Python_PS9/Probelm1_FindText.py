text  = open("Poem.txt")

content = text.read()

if("Twinkle" in content):
    print("The word Twinkle is present in file")
else:
    print("The word Twinkle is not present in file")