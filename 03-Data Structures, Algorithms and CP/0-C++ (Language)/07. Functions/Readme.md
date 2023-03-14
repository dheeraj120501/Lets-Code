- Functions are a piece of program code which performs a specific task.
- These are useful for procedural programming or modular programming.
- Collection of functions is called _library_.
- Every C++ function has a main function, the entry point of the program for what we want.

- We can break program into manageable, reusable pieces then piece wise development of code can be distributed among teams and then merged into single program in the end, main integrating them directly or indirectly. Also memory usage is more efficient here. This is modular programming achieved using functions.

## DECLARING A FUNCTION

- return type function_name(parameters list);

- A function can return atmost 1 value and not more than 1. Can take multiple inputs but gives 1 output.
- Functions not returning any values have type void.
- Rules for giving function names are same as variable names.

- We should avoid doing cin or cout inside the function as it is a bad function practice.
- Function shouldn't interact.

## How this works inside main memory ?

- Memory has 3 sections : Code section, stack and heap.
- Code section will have all the functions inside it. Like Global execution context.
- Machine code of functions is not copied into main that is a wrong belief. Machine code stays separate as per function.
- Program we are running, is loaded inside the code section.
- Whenever a function is called the memory for all the variables used in function is created inside the stack and when the function ends then all that memory is cleared automatically. If function allocated some memory into the heap, then that memory won't be deallocated on its own rather function should release it.

## Function Overloading

- Writing more than one function with the same name but different parameters.

- There would be name conflict in the case when return type is different but name of function along with parameters type and # of parameters are same.
  eg.
  ```cpp
  int max(int,int)
  float max(int,int)
  ```
- NOTE: The above is not function overloading. For function overloading either number of parameters or type of parameters should be different.

- C++ compiler can differentiate between 2 functions of same names based on parameters type and number of parameters being passed.

- 2 functions with same name and same number of parameters can be different too if data type of parameters is different.
- Benefit here is that if number or type of parameters is different then we don't need to think of new names coz the function is same only parameters type or number is different.

- Optional Parameters/ Default Parameters: We can pass the default parameters in functions, so the default parameters become Optional.

- Beware of side effects, particularly when it comes to the order that function parameters are evaluated. Do not use a variable that has a side effect applied more than once in a given statement.

- C++ allows passing or call by using 3 different methods

  1. Call by value or Pass by value
  2. Call by address
  3. Call by reference

- Call by value stores the values into the as the variables values' in activation record of function in stack memory. Creates a local copy, when the function ends that local copy is destroyed.
- Formal parameters are the parameters of the function we define and what we supply are actual parameters inside main. Formal parameters cannot modify the value of actual parameters.

- Call by address, in the function here we do not send the variables rather we send the address of variables. As we know that the address as value can only be stored by pointers so we make formal parameters as pointers in function definition above. This makes formal parameters as pointers to store address values and actual parameters passing their addresses to function.

- References are nickname to a variable and has to be initialized at the declaration time and can't be null. Syntax is same as call by value only at the definition of the function we use & ampersand.
- In call by reference changes can be done to actual parameters, Due to & being used i.e. reference variables being taken in function definition when we pass arguments inside main to the function new local copy is not created. Use call by reference when you want actual parameters to be modified.

## A BASIC SWAP VARIABLE EXAMPLE

- When we use call by reference what happens at machine code generation phase is that where we call swap function inside the main there machine code of swap function will be copied. Machine code of function will be copied inside the main function at the place of function call. It becomes part of main function and as a result during call by reference even if it seems another function directly modifying main function in reality before that happens another function becomes a part of main function. Temp is also created in the activation record of the main function itself and will be there as long as the swap funcion code is being executed.

- Loops inside call by references can lead to warnings as perfect copying of code by compiler might not happen.

- NOTE: We can have **data variables**, **address variables**(pointers), **reference variables**(nick names) So we can have functions that can pass and return data variables, address variables, reference variable.

## Demerits of Functions

- One don't need a function for absolutely every line of code that's not going to be good as it's going to be hard to maintain, your code is going to look messy and cluttered and it's actually going to make your program slower.
- Every time we call a function the compiler generates a call instruction i.e. in a running program in order for us to call a function we need to create the entire stack frame for the function meaning we have to push things like the parameters onto the stack we have to also push something called a return address onto the stack and then we actually jump to a different part of our binary in order to start executing the instructions from our function and that return value that we push we need to get back to where we originally were so this is called like jumping around memory in order to execute function instructions and all of that takes time so it slows down our program.
- Primary task of function is to prevent code duplication.

## Local VS Global variables

- Local variables remain in memory as long as the scope in which they are called is active, Global variables remain in memory as long as the program remains.
- Local variables are created in stack while global variables are created in code section.
- We can access global variables using :: scope resolution operator.

- Static Variables : These are variables which always reamins in the memory just as global variables only difference being that global variables can be accessed by any function but static variables are limited by their scope. Static variable is created only once and isn't created everytime, even if the function it is in is called multiple times.
- Static variables are global variables for a particular function.
- Static variables are useful inside the functions particularly in the modular or function based programming.
