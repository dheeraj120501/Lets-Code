#Nested functions and Closures
#A nested function is a function defined inside another function.
#It is created, used and destroyed dynamically, by the enclosing function, thus hiding it from the global scope.
#It has read only access of variables of the enclosing scope.

#Closure
# A closure is a nested function object that remembers values (read only) of the enclosing scope even if they are not present in memory.

#Decorators
#Python decorators are for adding functionality (code injection) into an existing code (wrapped function).
#This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

#Python decorators are implemented as Higher order functions that
#1) Take other functions (wrapped functions) as arguments.
#2) Create a nested function (wrapper function) which hosts meta code, invokes wrapped function through closure.
#3) Returns reference to nested function (wrapper functions).
#4) Updates wrapped function reference to refer to nested function (wrapper functions).

def make_odd(ptr_fx): # hof(wrapped_fn_reference)
    def worker(num): #wrapper fn
        temp = ptr_fx(num) #call to wrapped function
        if temp % 2 == 0:  #meta code
            return temp+1
        return temp
    return worker

@make_odd
def square(num):
    return num *num

@make_odd
def cube(num):
    return num *num * num


print(square(10))
print(square(9))
