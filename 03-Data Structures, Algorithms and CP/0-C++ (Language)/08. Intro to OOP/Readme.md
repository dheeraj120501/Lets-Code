# Introduction to OOP

Object orientation is a strategy/style of writing programs/software. Other methodologies include structured programming, procedural programming, modular programming, aspect oriented programming.

OOP is more related to designing of a software, and deals with internal designing or organization of code. Programming or app development becomes highly systematic and allows us to follow the procedures of engineering to design a software using OOP.

# Principles of Object Oriented Programming

1. **Abstraction**: Object Oriented approach gives a systematic method to develop software, apps and solutions in an organised way just how other engineers develop buildings, blue prints or any other things in a systematic manner.This allows the user to not know how the entire program works, just giving user enough idea about how to perform functions he/she wants to perform. Just like a TV or Car, internal mechanism is not available what user can interact with is more than enough to accomplish all the tasks users might need to perform. We write stuff inside class.

2. **Encapsulation**: Another thing we get due to class is encapsulation or data hiding.To avoid mishandling of variables we use data encapsulation. Functions used to access variables and modify them are public, but direct modification of variables is avoided by making variables inside a class as private.

3. **Inheritance**: Say we have written a class A, and after some days we want another class B which has all the features as class A along with some other features too which I will add. Then we can borrow/inherit all the features of A, add our own features to get class B.

4. **Polymorphism**: C++ polymorphism means that a call to a member function will cause a different function to be executed depending on the type of object that invokes the function.

# Class vs Object

It is said that everything in the world is an object and there is some class for it most probably. Class means to classify and we can take any object in the world and it has to belong to some class, even if it doesn't begins to any class then it means that it belongs to class of objects which do not fit into any other existing classes.

**Class is like a blueprint and object is the thing created from that blueprint.**

Class is a definition how something should be if it is made from the class, in a sense it is a blueprint. Object is the instance.

- Say Car is a class and BMW is an instance of it.
- Blueprint is made once but from that multiple houses are made which are identical in a housing board colony. That means that blueprint is a class telling how every house, an object should be and identical houses or objects are created from that.
- Data(attributes) and function(operations) together make up a class.
- We can create class for kind of object we want as per our needs and then create some instances of those classes we made to proceed as per our coding requirement.

**NOTE: Using dot operator(.) we can access the properties of a normal object. If we want to access the properties of a pointer object we use arrow operator(->).**

We can create an object either in stact or in heap just like any other primitive data type.

The concept of **getter and setter functions** are introduced because of data hiding/encapsulation.

- _getter_ is to get the data and setter is to set the data.
- Get functions are called accessor functions and set functions are called mutators and known as property functions.
- For a data member if there exists get and set both then that means it is read and writeable. If a data member has only get and no set then it means that data member is just read only. It depends on programmer to define read and write.

**CONSTRUCTOR** : A constructor function is a special member function that is a member of a class and has the same name as that class, used to create, and initialize objects of the class.

- On creation of object, a function was there in the compiler which constructed the object.
- Every class will have a constructor. Compiler provided built-in constuctor is called as default constructor.

- There are 3 different types of user defined constructor :
  1. Non-parameterized Constructor
  2. Parameterized Constructor
  3. Copy Constuctor
- If we don't write any of the 3 constuctors above then the 4th kind default constructor is provided by compiler.

- Contructor don't have any return type not even void and have name same as class name.

**PROBLEM WITH COPY CONSTUCTOR** : Copy constructer do shallow copy (naam ka copy bus). So whenever we have to deal with pointers we have to do deep copy (true copy). For deep copy we use heap memory (new and delete).

So our class should have the following methods irrespective of need to create a perfect class :

1.  Constructors
    - Non parameterized constructor
    - Parameterized constructor
    - Copy constructor
2.  Setter or mutators
3.  Accessors or Getters
4.  Actual functions useful for class called Facilitators
5.  Inspector function -> Checks based on some properties, mostly a bool
6.  Destructor function

In a class we just write the function names and do not define the functions inside it without ellaborating.
Functions are ellaborated outside the class by using `scope resolution operators`.

Every method of a class is automatically provided with a pointer named `this` that holds the address of the current object in which the method is called.

- this pointer is used to remove the ambiguity between parameters of functions and data members of a class.
- this is used to refer to the data member of current object we are writing this in.

A struct is another user defined data type. Data members can't be private or protected in a structure as opposed to a class. Structure has everything by default as public and class has everything by default as private.

# Data Hiding and Encapsulation

```c++
class Rectangle {
    public:
    	int length,breadth;
    	int area(){
            return length * breadth;
        }
    	int perimeter(){
            return 2*(length+breadth) ;
        }
};
```

Data hiding is related to encapsulation.

After encapsulation we move towards data hiding. Above we have a class which has data and functions on that data to do different things with data provided in class.

Inside a class by writing everything inside {} we are achieving encapsulation. But, above we have made everything public and it is not wise to allow direct access using className.dataMember to modify or manipulate the data Members of class as it may lead to mishandling of the variables which are then being passed on to functions.

- So data should be private and only the functions which are used to access that data should be public. Moreover having proper classes increases the reusability of the code too as it leads to functions which can be accessed and data which is private so everything performs as expected. Now to correct ourselves we make data members as private and functions as public.

```c++
class Rectangle {
    private:
    int length,breadth; // Making data members as private. Read and write of private isn't allowed.
    public:
    	int area(){
            return length * breadth;
        }
    	int perimeter(){
            return 2*(length+breadth) ;
        }
    	void setLength(int l){
            length = l; // Assigns the int l to the private data member length's value
        }
    	void setBreadth(int b){
            breadth = b; // Assigns the int l to the private data member length's value
        }
    	int getLength(){
            return length; // Returns the value of length which is a private data member
        }
    	int getBreadth(){
            return breadth; // Returns the value of breadth which is a private data member
        }
};
int main(){
    Rectangle r;
    r.setLength(5); // Object r has length = 10 which we set using function and not directly
    r.setBreadth(10); // Direct access of private data members isn't allowed so we use function
}
```

Now, we have not initialized the values inside the object of class Rectangle then how are we supposed to set the values for object.length and object.breadth ? To do so we make a function to set the length and breadth for an object as well as a function to read the value of length and breadth. But still mishandling can be done when we do `r.setLength(-10)` to avoid this we can instead set up an if condition inside function to check for incoming values as below and assign a default value in case value given to us is not what we would want to pass on to the functions after validating :

```c++
class Rectangle {
    private:
    int length,breadth; // Making data members as private. Read and write of private isn't allowed.
    public:
    	int area(){
            return length * breadth;
        }
    	int perimeter(){
            return 2*(length+breadth) ;
        }
    	void setLength(int l){
            if( l >= 0) // For checking if the value being entered is as per our liking
                length = l;
            else length = 0; // Valid default value
        }
    	void setBreadth(int b){
            if( b >= 0) // For checking if the value being entered is as per our liking
                breadth = b;
            else breadth = 0;
        }
    	int getLength(){
            return length;
        }
    	int getBreadth(){
            return breadth;
        }
};
int main(){
    Rectangle r;
    r.setLength(-5);
    r.setBreadth(10);
    cout << r.area() ; // Gives output as 0 because we pass length as negative.
    cout << r.getLength() ; // To print length of rectangle object r.
}
```

We will see later on how to send a message to main function when we do not get value as per our liking. Use get function to get value of data member, set to set the value of data member and make appropriate functions as per your needs. Get functions are called accessor functions and set functions are called mutators and known as property functions. For a data member if there exists get and set both then that means it is read and writeable. If a data member has only get and no set then it means that data member is just read only. It depends on programmer to define read and write.

Basically **access specifiers** are used for data hiding.

- Access modifiers (or access specifiers) are keywords in object-oriented languages that set the accessibility of classes, methods, and other members.
- The default access for members and classes is private.

Binding is the process of linking of the code associated with a procedure call.

- It may either Static or Dynamic.

In Dynamic Binding, the code is to be executed for a specific procedure call which is not known until run-time.

- Dynamic binding is also known as late binding or run-time binding.
- Dynamic binding is an object oriented programming concept and it is related with polymorphism and inheritance.

Message passing is a type of communication between processes or objects in computer science.

- In this model, processes or objects can send and receive messages (signals, functions, complex data structures, or data packets) to other processes or objects.

It is important to note that during memory allocation, every object is allocated memory for their seperate variables except static ones and the functions are not allocated to the object but to the class as they are common for all objects.

# Structures, Union, Enumerations

Enemuration consists of values known as enumerators, which represent integer constants.

- eg. enum Day { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY ,SATERDAY, SUNDAY};

Enumerated value can be used in place of int value and they can also use the tag name, to declare new variable.

```cpp
 Day workday=MONDAY;
 int offDay=SUNDAY;
```

One can also create anonymous enums.

```cpp
 enum {a, b};
```

# Singleton Pattern in C++
