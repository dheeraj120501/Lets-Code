# In Python programming, there are two types of arguments that can be passed in a function.
# positional arguments are the one in which an order has to be followed while passing arguments.
# keyword arguments
# * in case of arguments, refers to unpacking. Unpacking could be for a list, tuple, or a dictionary.
# args is a short form used for arguments. It is used to unpack an argument. In the case of *args, the argument could be a list or tuple.
# **kwargs is keyword arguments. It passes the data to the argument in the form of a dictionary.

# NOTE: args and kwargs are just names or identifiers we can name them anything the important thing is * and **.


# Positional arguments
def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)

# Keyword arguments and positional arguments
def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)