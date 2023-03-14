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


def make_beautiful(ptr_fx): #hof(wrapped_fun_ref)
    def worker_fx(x): #nested function (wrapper function)
        print('-----------') #meta code
        ptr_fx(x) #wrapped function called using the closure (memory object that stores address of the wrapped function)
        print('-----------') #meta code
    return worker_fx

@make_beautiful
def greet(whom): #Wrapped function
    print('Hello', whom)

greet('Student')
greet('Python')




