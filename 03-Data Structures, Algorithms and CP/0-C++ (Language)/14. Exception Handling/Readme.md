Exception handling is a feature of OOP.

There are usually 3 kinds of errors that occur in programming 1. Syntax Error: Programmer mistypes or skips writing something or writes it in an improper way then it leads to syntax error. This is usually caught by compiler on the step where we build the executable file (compile time error).

    2. Logical Error: Want to do task A but what happens is something unexpected, no errors in syntax but in expected output. These types of errors are difficult to remove as you have to think. Compiler won't help you but Pen and Paper
    will help for sure along with debugger.

    3. Run-time Error: Occurs when user is using an application and if user mishandles the app then app may cause error during the runtime of program. There were no errors during development phase but there exists error during
    runtime.
    e.g.(i) Bad Input -> Suppose user needs to give int but is entering a string then it will mess up the program for sure.
    (ii) Internet Connectivity.
    (iii) Deletion of crucial files required for proper functioning of program.
    (iv) Program dependent on a Printer or other hardware resource but that is not connected.

Program crashes abruptly during runtime errors. And it is users who are responsible for runtime error.

Exceptions are referred to as those inputs or cases upon entering of which program will give runtime error.

Thus, lack or inappropriate availability of resources causes Runtime errors which are external factors to the program.

    try {
        // conditions
    }
    catch(data_type var_name) {

    }

Inside try block if there is any error it will jump to the catch block and execute the statements specified there.
If there are no errors in try block, catch block won't be executed at all.
NOTE: If no error then run the entire try block, else go to catch block.

C++ compiler does not have any built-in mechanism for throwing the exception, rather we have to check for some conditions which may lead to error and based on that we have to throw exceptions. Java writes the code for throwing exception but C++ doesn't do that.

It doesn't matter what is it that you are throwing just throw something and same datatype should be put in catch block, and display your message inside the catch block.

Throw catch is just so that we can have a link between the point error occurs and connecting it to the code that tells what to show as error. You can do error code as well.

NOTE: Codes like this can be helpful in documentation you can give user a manual where you tell the user that this error code is thrown for this particular run time error.

Note on throw

    int division(int x,iny y)
    {
        if(y == 0)
            throw something;
        return x/y;
    }

- In the syntax above we can throw double,float,int,char and even string with message.

- We can write our own class, and we can throw an object of our class say MyException as well. If we are throwing our own class exception, it would be better to extend it from built-in class of C++ called exception, and we can inherit our class form that.

  class MyException
  {
  // something
  };
  int division(int x,iny y)
  {
  if(y == 0)
  throw MyException;
  return x/y;
  }

- Specifying empty throw( ) in front of your function means that function doesn't throws any exception.

int division (int x, int y) throw( ) // means no exception thrown.
{
return(x/y);
}

NOTE: The throw is catched by catch block. throw is also like a jump statement as it throw and get us out of the try block.

We can have catch block of multiple types and for exception of which we do not know which type it is of for that we do catch(...) this is called catch all. Exceptions are checked for in the order of catch. If you declare catch all in the beginning all exceptions will go to catch all in that case.

We can have try block inside try block i.e. nested try as well. Nesting of try and catch can be done as well.

If we have 2 classes, parent and child class, in that case if we have a try block and inside that there is a possibility of both the exceptions, so we will catch both the exceptions, we will have a catch each for parent and child class. First we specify catch for child class and after that catch for parent class as if we define exception of parent class first it is capable of handline and catching exception of child class as well.
