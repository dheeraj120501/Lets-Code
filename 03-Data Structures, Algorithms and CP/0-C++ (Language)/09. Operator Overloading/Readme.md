In C++ there are operators for various operations like +,-,*,/,new,delete etc.
These operators are meant for some specific data type. There are built-in operators for built-in data types.

Say + can be used by-default only with int or float data type only. If we are defining our own data type say a class called matrix and we want + operator to add 2 matrices A and B and store it in C ? 
With the help of operator overloading we can do so. + operator can be overloaded for matrix.
For user defined data type we can overload operators. There are various operators we can overload in C++ except a few.

For operator overloading two things are needed : 
1. How to write functions
2. Signature of a function

eg. Addition of complex number
Method: Complex add(Complex x)
Operator Overloading: Complex operator+(Complex x) // this can be called not as c3 = c1.operator+(c2) but as c3 = c1 + c2
c1 will be passed in `this` and c2 will be passed in x.


Friend function has to be written outside the class. Friend function can access every member of the class where it is declared friend. Independent function doesn't belongs to class but if friend of the class. That is the reason why scope resolution is not used with them.
NOTE: friend function will not have access to this.
We can also do operator overloading using friend function.

ANALOGY: Suppose 2 person have some money and they want to know total amount they both have. Either A can take B's money and find total or B can take A's money and find total. This is what kind of happens in operator overloading. Or what we can do is call a third person and tell him to take Money of A and B and tell the total. This is what happens when we use friend function. Above we can see how to make this friend function.

We can overload output stream or ostream operator as well. We use cout and cin i.e. instream and outstream for things like displaying the values or taking the input from the user. These extraction and insertion operators can also be over-loaded.

Just like operator overloading here we write the function first for displaying what we want and after that we would convert it into insertion operator overloaded form.