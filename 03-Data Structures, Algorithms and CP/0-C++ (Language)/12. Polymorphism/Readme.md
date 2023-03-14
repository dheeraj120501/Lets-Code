If we create object of Parent and call the function then function of parent will be called, if we create the function with same name in the child class and even if child inherits the parent publicly even then the function of child object will be called even though parent has the function with same name as the class child.

Writing the function with same name in child is function overriding. Already parent class has a function and child class inherits from parent and borrows that function but is redefining the function itself, in a way as if it's their own version.

In function overriding signature or prototype of the function stays same while there is a change in parameters in case of function overloading.

    Child c;
    c.display();
    c.Parent::display(); // To call display function of Parent

In Parent class pointer pointing to the object of child class, when we call an over rided function then Parent class function is called. To execute function of child class we do the following : we make the function of Parent as virtual.

NOTE: Generally functions that may be overrided in the child's class is made virtual, mainly with abstract class. Functions having virtual in front of them are there just for namesake and real functions are there down in derived class with definition that would be considered for final output.
virtual void fun2() = 0; //Pure virtual function

It is mandatory for derived classes to override the function when it is a pure virtual function.

If a class has pure virtual function then that class is known as abstract class. Object of that class cannot be created. However, pointer to the abstract class can be made Base *p ;.
Abstract classes can't have objects but they can have pointers to achieve polymorphism.
Base *p = new Derived();
p->fun2(); // Calls the function of derived class.

Pure virtual function used for getting polymorphism.

There are 3 types of classes in C++ : 1. A class having all concrete function no pure virtual function is implemented for reusability for child classes. 2. A class with all pure virtual function meant only for overriding i.e. polymorphism and such a base class is interface. // Abstract class 3. Class with some concrete functions and some virtual functions then purpose is reusability and polymorphism. // Abstract class
