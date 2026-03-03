class Demo:
    a=6

d1 = Demo()
print(d1.a) # 6 (Class Attribute is printed as there is no instance attribute 'a')
d1.a = 10
print(d1.a) # 10 (Instamce Attribute)
print(Demo.a) # 6 (Class Attribute)