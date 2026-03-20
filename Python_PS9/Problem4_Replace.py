word = ["Donkey", "Click", "Bad", "Shutup"]

with open("sample.txt","r")as f:
    content = f.read()
    
for w in word:
    content = content.replace(w, "#"*len(w))
        
    
with open("sample.txt","w")as f:
    f.write(content)     
    
   