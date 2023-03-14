# Higher order function: Functions that operate on other functions, either by taking them as arguments or by returning them, are called higher-order functions. 
# First class functions meaning functions are treated as values and can be send as arguments or can be returned.

def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum

a = funcret(1)
print(a)

def executor(func):
    func("this")

executor(print)

# Decorator takes a function and insert some new functionality in it without changing the function itself.
# A reference to a function is passed to a decorator and the decorator returns a modified function.
# The modified functions usually contain calls to the original function. This is also known as metaprogramming because a part of the program tries to modify and add functionality into another part of the program at compile time.
# A wrapper is a function that provides a wrap-around another function.
# The wrapper will take a function as argument
#NOTE decorator is called before defining a function.
# There are two ways to write a Python decorator:
    # 1. We can pass our function to the decorator as an argument, thus define a function and pass it to our decorator.
    # 2. We can simply use the @ symbol before the function we'd like to decorate.

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

# M1
# who_is_harry = dec1(who_is_harry)

# M2
@dec1
def who_is_harry():
    print("Harry is a good boy")

who_is_harry()