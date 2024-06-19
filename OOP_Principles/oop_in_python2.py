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

# -----------------Method Resolution Order (MRO)---------------------------------

# MRO is the order in which Python looks for a method in a hierarchy of classes.
# It is also known as C3 Linearization.
# Python uses the C3 linearization algorithm to determine the MRO.
# The MRO of a class can be viewed using the __mro__ attribute.
# The __mro__ attribute is a tuple that defines the method resolution order for a class.
# The MRO is determined by the order in which the base classes are defined in the class definition.

print(C.__mro__) # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

#---------------------Method Chainig--------------------------------------------
# Method chaining is a technique where multiple methods can be called in a single line.
# This is achieved by making the methods return self.
# This is also known as fluent interface or cascading.

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num
        return self

    def subtract(self, num):
        self.value -= num
        return self

    def multiply(self, num):
        self.value *= num
        return self

    def divide(self, num):
        self.value /= num
        return self

    def display(self):
        print(f"Value: {self.value}")

calc = Calculator(10) # value = 10
calc.add(5).subtract(3).multiply(2).divide(4).display() # Value: 6.0

#### Method Overriding is already demonstrated in "Polymorphism" in previous file: oop_in_python.py #######

# ---------------------Duck Typing--------------------------------------------
# Duck typing is a concept in programming that focuses on the behavior of an object rather than its class type.
# an object walks like a duck and quacks like a duck, then we can consider it as a duck, regardless of its actual type..
# In Python, this means that an object can be used in place of another object if it provides the same behavior (attributes and methods).
# This is different from static typing, where the type of an object is explicitly defined.
# In below example, Duck, Dog, and Cat classes have a walk method. The myfunc function takes an animal object and calls the walk method on it.
# Since all three classes have a walk method, they can be used interchangeably in the myfunc function.

class Duck:
    def walk(self):
        print("Duck is walking")

class Dog:
    def walk(self):
        print("Dog is walking")

class Cat:
    def walk(self):
        print("Cat is walking")

def myfunc(animal):
    animal.walk()

duck = Duck()
dog = Dog()
cat = Cat()

myfunc(duck) # Duck is walking
myfunc(dog) # Dog is walking
myfunc(cat) # Cat is walking
