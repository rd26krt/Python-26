# Multiple Inheritance
class A:
    def method1(self):
        print("A class method1 called")
        
class B(A):
    def method1(self):
        print("B class method1 called")
        super().method1()
        
class C(A):
    def method1(self):
        print("C class method1 called")
        super().method1()
        
class D(B,C):
    def method1(self):
        print("D class method1 called")
        super().method1()
        
d = D()
d.method1()

#multiple Inheritance
# B.method1(d)
# C.method1(d)
# A.method1(d)
