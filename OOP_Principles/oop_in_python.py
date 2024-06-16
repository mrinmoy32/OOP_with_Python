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