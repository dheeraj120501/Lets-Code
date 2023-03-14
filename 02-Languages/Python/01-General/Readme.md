## Computer

- A computer is a device that can execute programs.

## Program

- Program is a software entity designed and developed to automate a particular task.
- A program is composed of Code and Data.

## Code

- Code means instructions.
- For a task/subtask a set of instructions are grouped in a unit termed as a `function`.

## Function

- A function is a set (group) of instructions.
- It has a unique name for identification.
  - It performs a sub task for a program.
  - It requires a call for execution.

## Data

- Data means information.
- It is of two types:
  - Input: Input is the information that a program gets.
  - Output: Output is the information that a program generates.
- Program Data must be stored in a variable.

## Variable

- A variable is a reserved block in memory (RAM).
- It is identified by a unique name.
- It allows storage and retrieval of data.
- It can store one value at a time.
- Its value can change.

- Python doesnt have a specific variable declaration syntax.
- The variables get declared on first use (writing).
- On finding first use of a variable as writing, Python:
  1. Sense the datatype of the value being assigned.
     - Basic data types: int, float, str, bool, none
  2. Reserve memory corresponding to the datatype, in applications memory space.
  3. Register the declaration(a:1000) in a symbol table (dictionary).
  4. Assign the value to the memory location.

## Stream

- A stream is a channel of data transfer between interconnected devices.
- It may be unidirectional or bidirectional and accordingly it allows transfer of information.

## Standard Streams

- O/S establishes 3 streams and makes them available for use by the application (Python program).
  1. `sys.stdin`: Standard Input Stream for transfer of data from keyboard to application.
  2. `sys.stdout`: Standard Output Stream for transfer of data from the application to monitor.
  3. `sys.stderr`: Standard Error Stream for transfer of data from the application to monitor.

## Python

- Python does not enable you to code particularly close to the metal, as it is interpreted into C and then compiled.

## print()

- A predefined function that takes program data and transfers it to sys.stdout for rendering.

## input()

- A predefined function that fetches data from sys.stdin and assigns the same to program variables.

## Assignment Operator (=)

- Assignment operator (=) is used to read/evaluate the r-value/expression and assign the result to the variable address on the LHS.
- It returns the value that it assigns.
- It supports cascaded(cascading is kind of like chaining) usage.

- The `type()` function is used to find the type of the variable/value.

##Important Arithematic Operators

1. / : generates quotient of division to the accuracy until remainder becomes zero or a recurring value. Ideally a float value is generated.
2. // : generates integer quotient of division
3. % : generates remainder of integer division
4. \*\* : For exponentiation

- Python don't have unary operators like ++ or -- neither the ternary operator
  - For ternary operator it has 1 liner if else:
    ```python
    statement if(condition) else statement
    ```

## Understanding the Random library and how random numbers are created

## TypeCasting

- input() is used to accept values from keyboard, the data is receive in string (text) form, it may be converted to required form for further use.

- Typecasting don't change the type of the existing variables instead it return a new value of specified type so we can store it in other variable and use it

- int(string) attempt to convert the given string into an int (whole number).

  - When conversion is successful, an int value is returned.
  - When conversion fails, a ValueError is raised.

- int(), str(), bool(), ord(), chr()

## Taking List as a Parameter in Function

- Know that when a list is shared as parameter then the actual and formal parameters refer to the same list (memory). Hence updates are made to the common memory.
- This approach to data sharing between the caller and the called function is called as `Pass by reference`.

## Some cool swaping techniques:

1. Using 3 variables (creating a temporary varible):

   ```python
   c = a
   a = b
   b = c
   ```

2. Using just 2 variables (Arithematic method):

   ```python
   a = a + b
   b = a - b
   a = a - b
   ```

3. Using just 2 variables (Bit manipulation):

   ```python
   a = a^b
   b = a^b
   a = a^b
   ```

4. Python specific:
   ```python
   a,b = b,a
   ```

- **Comments** can be single line or multi-line.
- **Escape Sequence characters** are there so make sure to know about them.
- **Scoping** in python is done using indentation.
- To modify global variables we should use `global` keyword

## Operators Overview:

- Arithematic
- Assignment
- Comparison
- Logical
- Identity (is, is not)
- Membership (in, not in)
- Bitwise
