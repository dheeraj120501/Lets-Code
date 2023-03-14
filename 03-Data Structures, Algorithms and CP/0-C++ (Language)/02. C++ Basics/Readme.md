# Remember

Preprocessor directives, main(), output on console and input from console, cascading.

The return value from function main is called a status code, and it tells the operating system (and any other programs that called yours) whether your program executed successfully or not. By consensus a return value of 0 means success, and a positive return value means failure.

`\n` and `\t` and some other escape sequence in printing.

Difference in taking strings as input through `cin` or `getline()`.

Behaviour of `cin`, `cin.get()`, `cin.getline()`, `getline()`, `gets()` and `cout`.

# Variables

A `variable` is a reserved block in memory (RAM) .

- It is identified by a unique name.
- It allows storage and retrieval of data.
- It can store one value at a time.
- Its value can change.

Rules for naming a variable in C++

- Can only have alphabets, numbers and underscore.
- Cannot begin with a number.
- Cannot begin with an uppercase character.
- Cannot be a keyword defined in C++ language (like int is a keyword).

Compiler assigns a garbage value to the uninitialized local variable and null values(0, empty string) to uninitialized global variable.

## Local VS Global Variable

Local variables remain in memory as long as the scope in which they are called is active, Global variables remain in memory as long as the program remains.

Local variables are created in stack while global variables are created in code section.

We can access global variables using :: scope resolution operator.

## Static VS Instance Variable

Instance variables are basically variables of an object.

Static Variables : These are variables which always reamins in the memory just as global variables only difference being that global variables can be accessed by any function but static variables are limited by their scope. Static variable is initialized only once and isn't created everytime, even if the function it is in is called multiple times.

- Static variables are global variables for a particular scope in which they are defined like function or class.
- Static variables are useful inside the functions particularly in the modular or function based programming.

## Different type variables

A variable can be **data variable**, **address variable(pointer)**, **reference variable** based on what it store.

# Data Types

Data in a program is kept in variables which are capable of storing a certain kind of data formats called data types.

Data types are declarations for variables that determines the type and size of data associated with variables.

Computer memory is all filled with zeros and ones. If we have a problem and we want to code it it’s very difficult to provide the solution in terms of zeros and ones. To help users, programming languages and compilers provide us with data types.

- For example, integer takes 2 bytes (actual value depends on compiler), float takes 4 bytes, etc. This says that in memory we are combining 2 bytes (16 bits) and calling it an integer. Similarly, combining 4 bytes (32 bits) and calling it a float.
- NOTE: Data type is nothing it is based on how we store and interpreted/read 0,1 from memory.

**Data Types can be categorised into 3 types :**

1. Built-in Data Types (Primitives)
2. Derived Data Types
3. User-defined Data Types

![](https://i.imgur.com/2Ghc7Ky.png)

|   DATA TYPE   |      MEANING      |    SIZE     |
| :-----------: | :---------------: | :---------: |
|     bool      |      boolean      |  undefined  |
|     char      |     character     |   8-bits    |
|    wchar_t    |     wide char     |   16-bits   |
|   char16_t    |   unicode char    |   16-bits   |
|   char32_t    |   unicode char    |   32-bits   |
|     short     |   short integer   |   16-bits   |
|      int      |      integer      |   16-bits   |
|     long      |   long-integer    |   32-bits   |
|   long long   | very-long integer |   64-bits   |
| unsigned char | single-precision  |   32-bits   |
|     float     | double-precision  |   64-bits   |
|    double     | double-precision  | 10/16 bytes |

1 byte = 8 bits.

1 bit can either be 0 or 1.

Int can store values from -2147483648 to 2147483647.

Float is used to store upto 7 decimal digits whereas double is used to store upto 15 decimal digits.

Characters in C++ are enclosed inside single quotes.

Size of different data types.

- The C++ standard does not exactly specify the sizes of the any types, and the bounds depend on the compiler and platform.
- Number of bits each data type takes also depends on the programming languages, the compiler and the operating system it can change based on a system being 32-bit or 64-bit.
- Depending on the size of the data types, the total available values (domain) will also change.
- Nowadays, we have 64-bits machines, before that there were 32-bits and 16-bits machines before that. Mostly, in languages like C/C++ the size of integer depends upon the bit size of the machine.
- If machine is 16-bits then the integer by default takes 2 bytes (1 Byte = 8 bits), if machine is 64 bits then integer takes 8 bytes and so on.
- It is only applicable for integers, float always takes 4 bytes and char always takes 1 byte only, it is only the size of integer that depeneds on the bit-size of the machine.
- To check the size of a data type use the `sizeof` operator.
- The real difference between different data types is how much memory will be allocated when you create a variable with that data type.

  - At the most ground level even alphabets and characters are just numbers, and these numeric values to alphabets were assigned by **American Standard Code for Information Interchange ASCII**. Under this system A = 65, B = 66.....Z = 90. a = 97, b = 98... z = 122, Numeric 0 = 48 and 9 = 57.

- Type modifiers are used to modify the fundamental data types.

  - `signed`, `unsigned`, `long`, `short`.

- We can also turn these data types to pointers(\*) and references(&) by appending the required symbol to the type. eg. `int\*`, `int&`.

## Storing Data types

**Storing Decimal Number**: Sign bit(MSB) is used to store the sign of a number. To get the binary of a negitive decimal we just find the 2's complement of it's positive one.

- Say we want to store 10. Then 4 bits from right in order of writing from left to right would be 1010 in 16 bits it changes to 0000000000001010 for negative 10 first the binary form is complemented that is inversion of 0's and 1's with respect to positive version of the number so we get 1111111111110101 and this is called **1's complement**. Then 1 is added at the rightmost bit giving us 1111111111110110 and this is called **2's complement** of number. In any language the negative number is stored in the 2's complement form.
- Binary number is complemented called 1's complement and then added +1 to get 2's complement to get negative of original number we complemented, leading to MSB or leading bit becoming 1 for negative.

**Storing Floating Points**: Floating point numbers are stored in the form of mantissa and exponents.

**Storing Characters**: ASCII code is used to store characters in memory.

- Arithemetic operations on characters are done on their ASCII values.
- char + int gives an int unless specified externally.

## IEEE 754 floating point standard

This is the way a modern computer represents real numbers.

# Declaration VS Defination

Declaration mean informing to the compiler the following information: name of the variable, type of value it holds. i.e., declaration gives details about the properties of a variable for symbol table entry.

Definition of a variable says where the variable gets stored. i.e., memory for the variable is allocated during the definition of the variable.

- It mean allocating the memory and assigning the value.

They are mostly done together.

A variable or a function can be declared any number of times but, it can be defined only once.

A declaration introduces an identifier and describes itself, be it a type, object, or function. **A declaration is what the compiler needs to accept references to that identifier.**

- These are declarations:

```cpp
extern int bar;
extern int g(int, int);
double f(int, double); // extern can be omitted for function declarations
class foo; // no extern allowed for type declarations
```

A definition actually instantiates/implements the identifier. **It's what the linker needs in order to link references to those entities.**

- These are definitions corresponding to the above declarations:

```cpp
int bar;
int g(int lhs, int rhs) {return lhs*rhs;}
double f(int i, double d) {return i+d;}
class foo {};
```

A definition can be used in the place of a declaration.

An identifier can be declared as often as you want. Thus, the following is legal in C and C++:

```cpp
double f(int, double);
double f(int, double);
extern double f(int, double); // the same as the two above
extern double f(int, double);
```

- However, it must be defined exactly once. If you forget to define something that's been declared and referenced somewhere, then the linker doesn't know what to link references to and complains about a missing symbols. If you define something more than once, then the linker doesn't know which of the definitions to link references to and complains about duplicated symbols.

Literal is a direct value. eg. "Hello" is a String literal, 23 is a int literal etc.

For integer type of variables we can assign a literal in decimal number system, octal or hexa and these type of ints, can be used in short, long, long long and even for char data type.

- By default it's a base 10 integer, if prefixed with 0 it's Octal, if prefixed with 0x with Hexdecimal
- In `cout` all the system are converted to decimal and printed.
- In character all are converted to decimal and their ASCII values are printed.

To write float as 12.98 then by default the value is double. Better to have F or f at the end for float literals.

Similarly with integar it's int if you wanna assign long then use L suffix, and LL for long long.

NOTE: If we assign a float value to a char then float value is converted into character and this is done implicitly that's why it is called `type coercion`.

To use the number in scientific notation use e followed by the raised power. eg. 12e2 will be depicted as 1200, 12e-1 as 1.2 etc.

**`NOTE: Declaration in C/C++ are read in a spiral clockwise manner, https://c-faq.com/decl/spiral.anderson.html.`**

## Extern Keyword

A declaration can be done any number of times but definition only once.

The extern keyword is used to extend the visibility of variables/functions.

Since functions are visible throughout the program by default, the use of extern is not needed in function declarations or definitions. Its use is implicit.

When extern is used with a variable, it’s only declared, not defined.

As an exception, when an extern variable is declared with initialization, it is taken as the definition of the variable as well.

## Initialization

Initialization can be used to give a variable a value at the point of creation. C++ supports 3 types of initialization: **copy initialization**, **direct initialization**, and **uniform initialization** (also called list initialization or brace initialization).

```cpp
int a = 5, b = 6; // copy initialization
int c( 7 ), d( 8 ); // direct initialization
int e { 9 }, f { 10 }; // brace initialization (preferred)
```

Copy assignment (via operator=) can be used to assign an already created variable a value.

Initialization provides a variable with an initial value (at the point of creation). Assignment gives a variable a new value after the variable has already been defined.

One should prefer uniform initialization(braces initialization) over the other initialization forms, and prefer initialization over assignment (basically work with immutable data).

## Overflow

Say we have a char x and as we know the range of char is from -128 to 127 so we might get an error or warning upon storing 130 depending on compiler. So from char x = 127 if we do x++ in next line since the capacity of char is only till 127 max so it will come back to -128. Think of it as a round pattern with numbers from -128 to 127. If you do next or increment after last number 127 or 360 degree you come back to -128 or 0th degree. Similarly if we are at x = -128 and we do x-- then we come back to 127.

Cycling is done when the we try to exceed any data type's limit (overflow).

# Type Casting

Explicit type conversion => (newtype)var OR newtype(var)

- This doesn't change type of original variable but it creates a soft copy with new type which we can either store somewhere or use to print.
  eg.
  ```cpp
  int x = 65;
  cout<< char(x); //A
  cout<< (char)x; //A
  ```

# Type Alias Name

`typedef` used to define our own data type or giving alias to some other data type. So it is easier for us to keep track, prevent errors and make code more readable.
eg. typedef int i; //Now we can use i instead of int

- Above example gives alias to data type int used as i. Because we might not know what's the use of 2 int variables declared out of nowhere so it is better to have 2 int variables which are declared as i m1,m2 to give us an idea these something to do with marks.

- Most of the time typedef is used in competetive programming to make things fast. eg. typedef long long l.

**Modern way of giving types and alias name**: The syntax `using ll = long long;` is more modern.

- For a simple type definition it does exactly the same as `typedef long long ll;`
- But using supports template parameters, so the concept is more powerful.

```cpp
 template<typename T>
 using MyList = std::list<T, MyAlloc<T>>;

 MyList<Sometype> myList;
```

- Since a _typedef does not support template parameters_ we would need to 'misuse' a struct, something like this:

```cpp
  template<typename T>
  struct MyList {
    typedef std::list<T, MyAlloc<T>> type;
  };

  MyList<Sometype>::type myList;
```

# Declaring Constants

`Enum` is used to define a group of related constants under one name.

`#define` mon 0 //This is a preprocessor. As it is starting with # so no need of ; at the end.

int `const` mon = 0; //`const` keyword is used to make the path constant i.e. only read access.

- _NOTE path not storage._

# Header Files

Header files are traditionally used to declare certain types of functions so they can be used throughout your program.

We include header files using #include pre-processor directive in our cpp file which basically copy and paste that header file in that cpp file. Providing the cpp files with declarations.

Header gaurds are basically the checks on our header files so that they won't get included in our cpp files twice as the header files gets copied meaning we can't afford to copy the header files twice in our program.

- `#pragma once` a pre-processor directive that basically help us define our header file only once
- `#ifndef - #endif` same as pragma once used long ago.
  ```cpp
    #ifndef _FILE_H
    #define _FILE_H
    // codes
    #endif
  ```

The header files are sometimes included using `""` and other times using `<>` basically <> are used if the files are in our include directory and "" for anything else but mostly used for relative paths.

Some files are .h and others not(iostream) basically this is just one other way you can differentiate between what is in the C standard library and a C++ standard library.

# NOTE

% works only on int and char type data and not for float.

Arithematic Operators follow PEMDAS.

There are 4 kinds of pre/post increment and decrement operators.

1. Pre Increment (++x) Unary operator, much faster than x = x+1 a binary operator.
2. Post Increment (x++)
3. Pre Decrement (--x)
4. Post Decrement (x--)

- The increment and decrement operators can be used to easily increment or decrement numbers. Avoid the postfix versions of these operators whenever possible.

Bitwise operations occur on the bits of data and not on the entire data as single unit. Bit-Wise Operators which are available :

- & (bitwise AND) Takes two numbers as operands and does AND on every bit of two numbers. The result of AND is 1 only if both bits are 1.

- | (bitwise OR) Takes two numbers as operands and does OR on every bit of two numbers. The result of OR is 1 any of the two bits is 1.

- ^ (bitwise XOR) Takes two numbers as operands and does XOR on every bit of two numbers. The result of XOR is 1 if the two bits are different.

- << (left shift) Takes two numbers, left shifts the bits of the first operand, the second operand decides the number of places to shift. If a number x is left shift by i positions then result is x \* 2^i.Sign bit is not affected and stays same.

- \>\> (right shift) Takes two numbers, right shifts the bits of the first operand, > > the second operand decides the number of places to shift. > > If a number x is right shift by i then x will get divided by 2^i. Sign bit is not affected and stays same.

  - _The left shift(<<) filled the vacated positions with 0, a right shift(>>) will do the same only when the value is unsigned. If the value is signed then a right shift will fill the vacated bit positions with the sign bit or 0, whichever one is implementation-defined. If E1 in (E1>>E2) has a signed type and a negative value, the resulting value is implementation-defined. So the best option is to never right shift signed values._

- NOTE: Do not shift an expression by a negative number of bits or by greater than or equal to the number of bits that exist in the operand(E1). In short E2 should not be negitive and also should not be more than number of bits of E1.

  - `std::cout<<(3<<33)<<" "<<(3<<-1);`

- ~ (bitwise NOT) Takes one number and inverts all bits of it

**Operators are just functions that are already overloaded in standard cpp library.**
