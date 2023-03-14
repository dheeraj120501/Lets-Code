Code: Instructions to perform tasks.
    Python code can be organized in 3 ways:
        1) As script
        2) As functions
        3) As classes (to be discussed later)

    When Python code is directly written in the program it is treated like a script that executes from top to the botton.

    When Python code is composed as a function then it requires a call for execution. 
    On call, the program control jumps from the point of call to the definition of the function. Next the code of the function executes. Finally the program control jumps back (returns) to the statement following the call to the function.


Function (keyword: def)
    A function is a block of code that is designed to perform a
    sub task for the program.
    It is composed of 2 parts:
        1) Signature
        2) Body

    Signature notifies what a function does.
    It is composed of : 
        * Name of the function
        * Parameters (0 to many input data)

    Parameters:
        Parameters are values that are shared by the caller with the called function of a program.
        Parameters are of 2 types:
            * Actual
            * Formal
            Actual parameter is the value/variable that is passed along with the function call.
            Formal parameter is the variable (defined in the functions signature) that receives the data of the actual parameter and hence becomes of the data type as of the actual parameter.

    Body of the function contains instructions to perform the said sub task.
    It may optionally contain a return instruction for transferring back a solution (data).

    return
    return statement is optionally used in functions to:
        * causes termination of the function 
        * make the program control jump back to the caller of the function.

    Default values to parameters if given should be given from the rightmost parameters (from right to left only)


Nested functions and Closures
    A nested function is a function defined inside another function. 
    It is created, used and destroyed dynamically, by the enclosing function, thus hiding it from the global scope.
    It has read only access of variables of the enclosing scope.

    A Closure is a nested function object that remembers values of the enclosing scope even if they are not present in memory. 

Docstring:
    Docstring is a short form of documentation string. 
    Its purpose is to give the programmer a brief knowledge about the functionality of the function. It must be the first string in a function, and it is also an optional string but always good to have it while working on programs having multiple functions. 
    The syntax for writing a docstring is very simple as it is just a string written in between three double quotes placed three times (""" """) on either side of the string. 
    NOTE: It has to be the first line of code in the function’s body. 
    To call a docstring we write the name of the function followed by ._doc_