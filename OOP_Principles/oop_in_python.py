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