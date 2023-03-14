It is possible for base class pointer to point to derived class object.

class Base
{
public:
void func1();
void func2();
void func3();
}; // Base class with 3 functions created
class Child : public Base { // Class child inheriting from Base publicly
public:
void func4(); // Child class also has 2 additional functions along with 3 of class Base
void func5();
};
int main(){
Base *p; // To this pointer we assign an object of child class
p = new Child(); // It is possible for base class pointer to point to derived class object
// Now we can call the functions of the class to which we made the pointer initially i.e. Base
p->fun1();
p->fun2();
p->fun3(); // We can call all functions of class Base, to which we made Base *p;
// As pointer is of one class and object is of another class which inherits class one.
// Functions of the class of which pointer is will be called.
p->fun4; // Can't be done as pointer is of base class and all functions of base class only will be called. Even if object is of derived class, functions of derived class cannot be called.
}

Trying to create a pointer to child class and pointing it to base or parent class not possible.
Base class pointer pointing to the child class object can only call to the functions of base class.
