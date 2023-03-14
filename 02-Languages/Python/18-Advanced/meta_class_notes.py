# Python compiles the hl code and translate it into byte code and then interpreter interprets the byte code to machine code and runs it line by line on the fly

# Python compiler doesn't check for errors, the interpreter does that

# Python has first class function and supports higher order funtions


# Dunger/Magic/Data model methods
# These are used to do everything from scratch, the primitive datatypes are also classes and they already know what to do with the operators like what does int+ int do or what string + string do now when we create a new data type using class we can also make how the operators work like what to do when we print the operator or what to do when 2 such data types are added or have >, <, == etc operators with them, all these are done using dunger methods.

# eg. 
# __repr__(self): what to do when we print the object
# __mul__(self): what to do when we use * operator with the object


# Metaclasses: Defines rules for a class, have to inherit type
# __new__ is always called first, modifies the construction of the class
# Default metaclass of any class is type
# We can explicitly change that like class Dog(metaclass=Meta), where Meta is another Metaclass defined by us
# Class is of type type()
# type() is used to make class it takes 3 arguments
# First the className, second the parent/base class, third the attributes

class Mammal:
    def sayHi(self):
        print("HI")

def sayHello(self): 
    print("Hello")

Dog = type("Dog",(Mammal,),{'legs': 4, 'sayHello': sayHello,})

jimmy = Dog()

print(jimmy.legs)
jimmy.sayHi()
jimmy.sayHello()

# Context Manager 