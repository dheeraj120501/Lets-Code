Inheritance : One of the important features of OOP. Acquiring the features of existing class into a new class is inheritance, i.e. deriving a class from existing class.


isA vs hasA Relationship: This concept is useful for understanding access specifiers in C++ and applies to Object Orientation in general.

Class can be used in 2 ways : 
    (i) By inheriting/deriving
    (ii) By creating its object

Say we have a class Rectangle and from that we make a class called Cuboid which inherits Rectangle publicly. So, here we can say that since Cuboid inherits rectangle so Cuboid can be considered as modified Rectangle only. So, when we inherit a class we will say that Cuboid is a (isA) Rectangle.

See another example, say there is separate class Table, Rectangle top as an object among other functions. Here we say that as Table class uses object of Rectangle named top we consider it as Table has a Rectangle. So, when we use a class by creating an object of that class then we will say that Table has a (hasA) Rectangle.

Classes can have data members of 3 kinds 
    (i) Public 
    (ii) Private 
    (iii) Protected

Public, private and protected are access specifiers in C++.
Function can accesses members of parent but can access protected and public not private. Private is available but not accessible in child, public and protected are accessible via child too in a class.


Types of Inheritance :

1. Single / Simple Inheritance: If we have class A as parent having class B as it's child class . So, class B is inheriting from existing class. This is single/simple inheritance.

2. Hierarchical Inheritance: If we have class A and from this class more than 1 class i.e. class B, C and D are inheriting then this is called Hierarchical Inheritance. 

3. Multilevel Inheritance: If there is a parent class A and from that class there is class B is inheriting and from class B there is class C inheriting then this is known as Multilevel inheritance.

4. Multiple Inheritance: If there are 2 classes A and B on the same level and from both of them a single class is inheriting i.e. class C then this is called Multiple Inheritance. This is a unique kind of inheritance supported in C++. This is not allowed in JAVA. Due to this for one class there can be one or more base classes.

5. Hybrid Inheritance: There is another kind of inheritance known as hybrid inheritance where we mix different kinds of inheritance models known to us.

Mixing of hierarchical and multiple or various other kinds of inheritance together gives us hybrid inheritance. Say from parent class A there is inheritance of base classes B and C, and from these two there is another class which inherits i.e. D. This is an example of hybrid inheritance. Where from top we see hierarchical inheritance and at the bottom it is multiple inheritance. This type of inheritance is unique to C++ but on having this kind of inheritance then features of base class A will appear in D via B and C both. Say A has function fun() then this function will be available via B and C class to class D. On calling the function we see there are 2 copies of functions in D which comes from B and C. This is what is known as multi-path inheritance.

Diamond shape problem: Here ambiguity we face is to call fun( ) function via B or C. To tackle this we have concept of virtual base classes.

   class A {
       // Some stuff inside the class.
   };
   class B : virtual public A // See here we use virtual
   {
       // Some more stuff inside the class.
   };
   class C : virtual public A // Another class same as B
   {
       
   };
   class D : public B, public C
   {
   	// Due to writing virtual then ambiguity is removed of function appearing via B or C
   };
   

Ways of Inheritance: There are more than one way of deriving a child class from parent class. There are 3 methods of inheritance i.e.. public, private and protected. By default everything in a class is private.

Public Inheritence:
    class child : public Parent

    Say there is a class called Parent and has 3 members, private, protected and public. We have a class called child which publicly inherits from the Parent class. Child also has 3 members, private, protected and public. On inheriting from parent class everything is available in children class but only protected and public members are accessible. Protected becomes protected on coming to child class and public element of parent stays public in child class.

Protected Inheritance:
    class child : protected Parent
    class GrandChild : public child

    Here protected member stays protected but the public member of Parent class also becomes protected. When GrandChild class inherits from the public child then also public of parent will be inherited in GrandChild as protected.

    NOTE: Way of inheritance affects the objects and grand child classes or sub classes which are subsequently formed.

Private Inheritance:
    class child : private Parent
    class GrandChild : public child

    Doing above leads to both protected and public members of Parent class becoming private. So due to that GrandChild is unable to access any of the members of the Parent class.


Generalizations vs Specialization
 
A group of class when given a general term easy for reference or a super class which contains all similar classes which can be identified by common name is what's called Generalization of classes. 
If parent exists and child inherits from parent then that top down approach is Specialization. 
If children elements are integrated into one big parent umbrella after they were created that is the case of Generalization. In generalization base class doesn't have anything to give to child class, it's only purpose is to put children into one super class which can be used to reference similar kinds of classes. Generalization is needed for polymorphism. That is same name but different objects and different actions.

Purpose of generalization is to achieve polymorphism and purpose of specialization is to give its child elements some features as parent. So purpose of Inheritance are 2 basic things : Sharing features to child classes and second is to achieve polymorphism.