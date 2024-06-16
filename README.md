# OOP with Python

Object-oriented programming (OOP) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphism, encapsulation, etc. in programming. The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

## Table of Contents
1. [Classes and Objects](#classes-and-objects)
2. [Inheritance](#inheritance)
3. [Polymorphism](#polymorphism)
4. [Encapsulation](#encapsulation)
5. [Abstraction](#abstraction)
6. [Composition](#composition)
7. [Aggregation](#aggregation)
8. [Association](#association)

## Classes and Objects
A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). An object is an instance of a class. When a class is defined, no memory is allocated but when it is instantiated (i.e. an object is created) memory is allocated.

```python
# Define a class
class Car:
    # Class attribute
    wheels = 4

    # Constructor method
    def __init__(self, make, model):
        # Instance attributes
        self.make = make
        self.model = model

    # Instance method
    def drive(self):
        print(f"The {self.make} {self.model} is driving.")

    # Another instance method
    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry")

# Access instance attributes
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry

# Access class attribute
print(my_car.wheels)  # Output: 4

# Call instance methods
my_car.drive()  # Output: The Toyota Camry is driving.
my_car.stop()  # Output: The Toyota Camry has stopped.
```
## Inheritance
Inheritance is a mechanism in which one class acquires the properties and behavior of another class.

```python
# Inheritance using super() method
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"The {self.make} {self.model} is charging.")

# Create an instance of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model S", 100)

# Access inherited attributes and methods
print(my_electric_car.make)  # Output: Tesla
my_electric_car.charge()  # Output: The Tesla Model S is charging.
```

## Polymorphism
Polymorphism means having many forms. In Python, polymorphism allows us to define methods in the child class with the same name as defined in their parent class. This is known as method overriding.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

animals = [Dog("Buddy"), Cat("Misty"), Dog("Max")]

for animal in animals:
    print(animal.speak())
```

## Encapsulation
Encapsulation is the bundling of data (attributes) and methods into a single unit or class. It restricts direct access to some of an object's components, which prevents the "accidental modification" of data.

```python
class Person:
    def __init__(self, name, age):
        self._name = name  # protected attribute
        self._age = age  # protected attribute

    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

person = Person("Alice", 30)
person.display()  # Output: Name: Alice, Age: 30
person.set_name("Bob")
person.display()  # Output: Name: Bob, Age: 30
```

## Abstraction
Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. It helps in reducing programming complexity and effort.

```python
from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, initial_balance, interest_rate):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Calculated interest: ${interest}")

savings_account = SavingsAccount("123456", 1000, 5)
savings_account.calculate_interest()  # Output: Calculated interest: $65.0
```

## Composition
Composition is a design principle in which one class is composed of one or more objects from other classes, meaning that the composed class has objects of other classes as attributes.

```python
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Bike:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Bike starting")
        self.engine.start()

    def stop(self):
        print("Bike stopping")
        self.engine.stop()

bike = Bike()
bike.start()  # Output: Bike starting, Engine started
bike.stop()  # Output: Bike stopping, Engine stopped
```

## Aggregation
Aggregation is a special form of association where one class is a part of another class, but both can exist independently.

```python
class Wheel:
    def __init__(self, diameter):
        self.diameter = diameter

    def display(self):
        print(f"Wheel diameter: {self.diameter}")

class Rickshaw:
    def __init__(self, wheels):
        self.wheels = wheels

    def display(self):
        for wheel in self.wheels:
            wheel.display()

wheel1 = Wheel(20)
wheel2 = Wheel(10)
wheel3 = Wheel(25)
wheel4 = Wheel(45)
wheels = [wheel1, wheel2, wheel3, wheel4]
rickshaw = Rickshaw(wheels)
rickshaw.display()  # Output: Wheel diameter: 20, Wheel diameter: 10, Wheel diameter: 25, Wheel diameter: 45
```

## Association
Association defines a relationship between classes of objects that allows one object instance to cause another to perform an action on its behalf.

```python
class Driver:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Driver: {self.name}")

class Taxi:
    def __init__(self, driver):
        self.driver = driver

    def display(self):
        self.driver.display()

driver = Driver("Alice")
taxi = Taxi(driver)
taxi.display()  # Output: Driver: Alice
```
```