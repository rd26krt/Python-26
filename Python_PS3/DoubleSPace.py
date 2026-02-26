sentence = "Rohan is a good boy  boy"
print(sentence.find("  "))

offerLetter = '''Dear <|{name}|>,
You are selected,

<|{date}|>'''
print(offerLetter.replace("<|{name}|>", "Rohan").replace("<|{date}|>", "24.07.2026"))