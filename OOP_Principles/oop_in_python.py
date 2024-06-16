# Object-oriented programming (OOP) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphism, encapsulation, etc. in programming. The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

#-------------------------- Classes and Objects --------------------------------
# A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
# An object is an instance of a class. When a class is defined, no memory is allocated but when it is instantiated (i.e. an object is created) memory is allocated.

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

###################### Create an instance of the Car class #####################
my_car = Car("Toyota", "Camry")

# Access instance attributes
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry

# Access class attribute
print(my_car.wheels)  # Output: 4

# Call instance methods
my_car.drive()  # Output: The Toyota Camry is driving.
my_car.stop()  # Output: The Toyota Camry has stopped.

# Modify instance attribute
my_car.make = "Honda"
print(my_car.make)  # Output: Honda

# Modify class attribute
Car.wheels = 6
print(my_car.wheels)  # Output: 6

##################### Create another instance of the Car class ##################
another_car = Car("Ford", "Fusion")

# Access class attribute
print(another_car.wheels)  # Output: 6

# Call instance methods
another_car.drive()  # Output: The Ford Fusion is driving.

################## Importing the BankAccount class from bank_account.py ##################
from bank_account import BankAccount

new_account = BankAccount("987654321", 500)
print(new_account.get_balance()) # Output: 500
new_account.deposit(100) # Output: Deposited $100. New balance: $600
new_account.withdraw(50) # Output: Withdrew $50. New balance: $550
print(new_account.get_balance()) # Output: 550

#-------------------------- Inheritance --------------------------------
# Inheritance is a mechanism in which one class acquires the properties and behavior of another class.
# Inheritance using super() method
# The super() method is used to call the constructor of the parent class (superclass). It is used to call the constructor of the superclass and to access all the methods and attributes of the superclass.
# In the following example, the ElectricCar class inherits from the Car class. The ElectricCar class has an additional attribute battery_capacity and a method charge().

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"The {self.make} {self.model} is charging.")

class ColoredCar(Car):
    def __init__(self, make, model, color):
        super().__init__(make, model)
        self.color = color

    def display(self):
        print(f"The {self.make} {self.model} is {self.color} in color")

# Create an instance of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model S", 100)

# Access inherited attributes
print(my_electric_car.make)  # Output: Tesla
print(my_electric_car.model)  # Output: Model S
print(my_electric_car.wheels)  # Output: 4

# Access subclass attribute
print(my_electric_car.battery_capacity)  # Output: 100

# Call inherited methods
my_electric_car.drive()  # Output: The Tesla Model S is driving.
my_electric_car.stop()  # Output: The Tesla Model S has stopped.

# Call subclass method
my_electric_car.charge()  # Output: The Tesla Model S is charging.

my_colored_car = ColoredCar("BMW", "X5", "Red")
my_colored_car.display()  # Output: The BMW X5 is Red in color

#-------------------------- Polymorphism --------------------------------
# Ploymorphism means having many forms. In Python, polymorphism allows us to define methods in the child class with the same name as defined in their parent class. This is known as method overriding.
# Ploymporphism using method overriding
# Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already provided by its superclass.
# When a method in a subclass has the same name, same parameters or signature, and same return type as a method in its superclass, then the method in the subclass is said to override the method in the superclass.
# In below example, the speak() method is overridden in the Dog and Cat classes.

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

#-------------------------- Encapsulation --------------------------------
# Encapsulation is the bundling of data (attributes) and methods into a single unit or class. It restricts direct access to some of an object's components, which prevents the "accidental modification" of data.
# Encapsulation using private attributes and methods
# In Python, we can denote private attributes and methods by prefixing the attribute or method name with double underscores __. This makes the attribute or method private, and it cannot be accessed directly from outside the class.
# We can define getter and setter methods to access and modify the private attributes.
# In the following example, the Person class has private attributes _name and _age. We have defined getter and setter methods to access and modify these attributes.


class Person:
    def __init__(self, name, age):
        self._name = name # protected attribute. notice the underscore
        self._age = age # protected attribute. notice the underscore

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
# Recommended way to access and modify private attributes
print(person.get_name())  # Output: Alice
person.set_name("Bob")
person.display()  # Output: Name: Bob, Age: 30
print(person.get_age()) # Output: 30
person.set_age(25)
person.display()  # Output: Name: Bob, Age: 25

person.name = "Charlie"  # This will not change the name attribute
person._name = "Charlie"  # This will change the name attribute but it's not recommended
person.display()  # Output: Name: Charlie, Age: 25

person.age = 45  # This will not change the age attribute
person._age = 45 # This will change the age attribute but it's not recommended
person.display()  # Output: Name: Charlie, Age: 45

#-------------------------- Abstraction --------------------------------
# Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. It helps in reducing programming complexity and effort.
# Abstraction using abstract classes and methods
# In Python, we can create abstract classes using the abc module. Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared, but contains no implementation.
# Abstract classes cannot be instantiated, and their abstract methods must be implemented by their subclasses.
# In the following example, the Device class is an abstract class with two abstract methods turn_on() and turn_off(). The Laptop and Smartphone classes inherit from the Device class and implement the abstract methods.

from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod # @ stands for decorator
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
    
    def display_model(self):
        print(f"{self.brand} {self.model}")
    
class Laptop(Device):
    def turn_on(self):
        print(f"{self.brand} {self.model} is turning on")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turning off")

class Smartphone(Device):
    def turn_on(self):
        print(f"{self.brand} {self.model} is turning on")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turning off")

laptop = Laptop("Dell", "Inspiron")
laptop.display_model()  # Output: Dell Inspiron
laptop.turn_on()  # Output: Dell Inspiron is turning on
laptop.turn_off()  # Output: Dell Inspiron is turning off

smartphone = Smartphone("Apple", "iPhone 12")
smartphone.display_model()  # Output: Apple iPhone 12
smartphone.turn_on()  # Output: Apple iPhone 12 is turning on
smartphone.turn_off()  # Output: Apple iPhone 12 is turning off

# Below are some design principles that are not part of the four pillars of OOP but are important in OOP as design principles.

#-------------------------- Composition --------------------------------
# Composition is a design principle in OOP that models a has-a relationship. It enables creating complex types by combining objects of other types.
# In composition, the objects that are part of the other object can exist independently. If the parent object is destroyed, the child objects can continue to exist.
# In the following example, the Engine class is composed within the Bike class. The Bike class has an engine attribute that is an instance of the Engine class. 

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

#-------------------------- Aggregation --------------------------------
# Aggregation is a design principle in OOP that models a has-a relationship. It is a more specialized form of association where objects have a reference to another object, but the objects can exist independently.
# In aggregation, the child objects can exist independently of the parent object. If the parent object is destroyed, the child objects can continue to exist.
# In the following example, the Wheel class is aggregated within the Rickshaw class. The Rickshaw class has a list of Wheel objects.

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
rickshaw.display() # Output: Wheel diameter: 20, Wheel diameter: 10, Wheel diameter: 25, Wheel diameter: 45

#-------------------------- Association --------------------------------
# Association is a design principle in OOP that models a has-a relationship. It is a more general form of relationship where objects have a reference to another object.
# In association, the objects that are part of the other object can exist independently. If the parent object is destroyed, the child objects can continue to exist.
# In the following example, the Driver class is associated with the Taxi class. The Taxi class has a driver attribute that is an instance of the Driver class.

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
taxi.display() # Output: Driver: Alice

#-------------------------- Dependency --------------------------------
# Dependency is a design principle in OOP that models a uses-a relationship. It is a more temporary form of relationship where objects depend on each other for a short period of time.
# In dependency, the objects that are part of the other object cannot exist independently. If the parent object is destroyed, the child objects cannot continue to exist.
# In the following example, the Car class depends on the Engine class. The Car class has an engine attribute that is an instance of the Engine class.

class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car starting")
        self.engine.start()

    def stop(self):
        print("Car stopping")
        self.engine.stop()

car = Car()
car.start()  # Output: Car starting, Engine started
car.stop()  # Output: Car stopping, Engine stopped