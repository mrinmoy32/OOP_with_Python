# ------------------------multilvel inheritance----------------------------

# Multilevel inheritance is when a class is derived from a class which is also derived from another class.
# class A is parent class of class B and class B is parent class of class C
# This is kind of like prototypal inheritance in JavaScript

class A:
    a = 5

    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B(A): # B is inheriting A
    b = 10

    def feature3(self):
        print("Feature 3 is working")

class C(B): # C is inheriting B
    c = 15

    def feature4(self):
        print("Feature 4 is working")
    
a1 = A()
print(a1.a) # 5
a1.feature1() # Feature 1 is working 
a1.feature2() # Feature 2 is working

b1 = B()
print(b1.a) # 5 (inherited from A)
print(b1.b) # 10 (B's own)
b1.feature1() # Feature 1 is working (inherited from A)
b1.feature2() # Feature 2 is working (inherited from A)
b1.feature3() # Feature 3 is working  (B's own)

c1 = C()
print(c1.a) # 5 (inherited from A)
print(c1.b) # 10 (inherited from B)
print(c1.c) # 15 (C's own)
c1.feature1() # Feature 1 is working 
c1.feature2() # Feature 2 is working
c1.feature3() # Feature 3 is working 
c1.feature4() # Feature 4 is working

# ------------------------multiple inheritance----------------------------

# Multiple inheritance is when a class inherits from more than one parent class.
# class C is inheriting A and B

class A:
    a = 5

    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
    
class B:
    b = 10

    def feature3(self):
        print("Feature 3 is working")
    
class C(A, B): # C is inheriting A and B
    c = 15

    def feature4(self):
        print("Feature 4 is working")
    
a1 = A()
print(a1.a) # 5
a1.feature1() # Feature 1 is working
a1.feature2() # Feature 2 is working

b1 = B()
print(b1.b) # 10
b1.feature3() # Feature 3 is working

c1 = C()
print(c1.a) # 5 (inherited from A)
print(c1.b) # 10 (inherited from B)
print(c1.c) # 15 (C's own)
c1.feature1() # Feature 1 is working (inherited from A)
c1.feature2() # Feature 2 is working (inherited from A)
c1.feature3() # Feature 3 is working (inherited from B)
c1.feature4() # Feature 4 is working (C's own)