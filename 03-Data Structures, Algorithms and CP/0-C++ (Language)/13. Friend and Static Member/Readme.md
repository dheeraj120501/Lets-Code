Friend functions are global functions that are not a member of the class but can access the private, protected and public members of that class, and can access and manipulate values even from outside upon object but not directly.

Used for operator overloading mostly.

Friend classes: To allow one class to access private members of another class upon object, we make it friend class.

NOTE: This is unlike inheritence so to access the members in friend class/ function we need to create the object of the other class first.

Static variable occupies memory only once. Static variables or static data members belongs to a class and not to an object. Objects can share it. There is only one copy of static members and all objects share it.
When there is a static member inside the class then we are supposed to declare it outside the class as well, again but as we want it accessible only inside that class so we do scope resolution wrt that class.

Like static members, static functions can also be accessed using the class name with scope resolution operator.

Conclusion :

1. Class can have static data members as well.
2. There will be only one instance which leads to memory being allocated only once.
3. All objects share that data member.
4. We can have static member functions as well to access the static members we declared as public inside the class.
5. Static member function can only access static data members.
6. 2 times you have to declare static data members. Once inside and other outside the class.
7. Static members can be accessed by using the object or the class with scope resolution operator.

Inner class basically is writing one class inside another class. So that subset class is useful only inside parent class.
Ideal for conditions where we want a class inside a class and subset class is not useful anywhere else.
We use it to reduce the complexity of bigger class we can write the code inside it in smaller classes.

Object creation always done after the definition of the class only.

Inner class can access the members of outer class iff they are static.

Outer class can create the object of Inner class and using that object it can access all the members of Inner class. The outer class can access all the members of the Inner class just like it is a class outside. But we write it inside Outer class to make it available inside Outer class only.

Nested class is a limited scope class which is visible only inside the outer class.
Outer::Inner a; // Creating Object of Inner class.
