# Conditionals

In C++ false is 0 and any other value is 1 or true. Conditional statements are prepared using relational operators.

- Relational Operators are :

  1. `<` Less than
  1. `<=` Less than equal to
  1. `>` Greater than
  1. `>=` Greather than equal to
  1. `==` whether equal to
  1. `!=` Not equal to

Logical Operators : To combine two or more than two conditions

- Logical Operators are :
  - && AND
  - || OR
  - ! NOT
- Remember about **SHORT CIRCUTING**

# Scopes

When we do not need a variable throughout the program but only to check a condition. We can either create an empty block and enclose the variable we want to limit in scope using {} which is called a _Dummy Block_, because in C++ scopes are defined by {}.

eg.

```cpp
{
int c = a + b;
cout << c << endl;
}
cout<<c; // can't access c here
```

OR

```cpp
if (int c = a + b; c > 10) // Available only in C++ 17.
{
cout << "Sum is greater than 10.\n";
}
cout<<c; // can't access c here
```

C++ allows declaration of variables as per our needs within a specified scope or throughout the program that's our choice.
In C we were supposed to declare all the variables in the beginning of a program at one place.
In above example based on some if condition we declare c and use it to print sum and outside the {} c variable won't exist.

# Switch

Switch case is a branch and control statement. Construct of switch case looks like following :

```cpp
switch (expression) // NOTE : Expression can be int or char type variable.
{
case 1:
code for case 1
break;
case 2:
code for case 2
break;
default:
code for default case (OPTIONAL), if break written anywhere other than last then use break.
}
```

SWITCH cases are used for menu-driven programs where user has choices to select from, for every case we write a code.
We can have nested switch cases as well.
NOTE: If we don't use break in any case the code will continue to go down untill it gets a break.

# Ternary Operators

Ternary operators are there for conditional assignment while if-else for conditional execution.

There's actually two things that happen when we write an if statement the evaluation of the actual condition and the branch depending on that evaluation, so if our condition evaluates to true we need to jump to a certain part of our source code and if it evaluates to false we need to jump to another part of our source code which in a running application is the machine instructions.

- Basically we branch to one section of our machine code (CPU instructions) or we branch to another section of our CPU instructions depending upon the evaluation of the condition.

When we start an application that entire application along with all of its modules gets loaded into memory so basically all those instructions that make up our program are stored in memory and when we have a condition that results in a branch basically mean telling the computer to jump to different part of our memory and start executing the instructions from there.

- Because of all that jumping around memory, if statements and branches in general do carry a little bit of overhead.

There is no `else if` in cpp basically an else if is

```cpp
else {
    if() {}
}
```

# Branchless Programming

Branchless programming is a technique to gain speed in our high and low level programming by avoiding branching code as much as possible.
