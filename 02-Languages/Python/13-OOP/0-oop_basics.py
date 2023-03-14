# Everything in Python is an Object
# Class is used to create user defined data types

class Dog(object) :
    def __init__(self, name, age = 10):  # This is the constructor that will first run when an instance of this class is constructed
        # Optional parameters are also available with Class methods and constructors
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"Hello {self.name},  U are {self.age} y/o")

jimmy = Dog("Jimmy", 12)
jimmy.speak()
print(jimmy.name)

class Cat(Dog) :
    def __init__(self, name, age, color):
        super().__init__(name, age)    # Super means the parent class (Dog here)
        self.color = color
    
    def speak(self):
        super().speak() # this will first execute parent's speak method
        print("Meow")

kitty = Cat("Angel", 8, 'green')
kitty.speak()

# Every method of Class except static method has a self which is provided automatically, this self contain the address of the object.
 
# Overriding methods, we can override methods of parent class

# Decorators used for special methods
# @classmethod needs to pass cls which acts like self, so we don't need to make the object of the class to run this method
# @classmethod is used as alternative constructor
# @staticmethod don't have cls/ self so we don't have access to any of the class properties/ methods, so we don't need to make the object of the class to run this method
# Any normal method take self as parameter, so we need to make the object of the class to run this method

# Public and Private are not in Python
# anything with _ at start mean protected just as a convention
# anything with __ at start mean private just as a convention but just in case we don't use this by mistake python do name mangling meaning they change the name slightly
#   eg. let say in a class A we have a variable __a then name mangling change the name to _A__a meanning it add __className at the start

# How object search for properties: first they check if that is a instance var of the class then check if it is an instance var of any parent class if not then check if it is the class var of current class if not then check if it is class ver of the parent class if not then it show error.
# NOTE if the parent's constructor is overridden then it won't search for the instance var in parent class.
# NOTE instance var are always present in __init__ i.e.(constructor)
# NOTE super() is used to access the properties of parent class