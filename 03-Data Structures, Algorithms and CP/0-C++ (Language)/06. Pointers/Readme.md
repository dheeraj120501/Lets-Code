- Pointers are a type of variable in C++. Pointer is a variable which is used to store the address of the data.
- Based on type of data stored variables can be categorized into 2 kinds :

  1. Data Variables (Used to store data)
  2. Address Variables (Used for storing address)

## Why use Pointers

- Suppose there is main function, and whatever is there inside main gets converted into machine code. We may have other functions as well but for the sake of simplicity let's assume here that main function contains your entire program.

  - As we know there are 3 sections in a program : **Code Section, Stack and Heap**
  - Our program i.e. stuff inside main is in code section and it can either access the same code section or the stack above it but it cannot access heap directly.
  - Program has a policy of not accessing anything else directly in the system except stack and code section. So, a program can't directly access heap, but indirectly program can access heap, by declaring a pointer which is in stack and that pointer can have address of a memory in heap .
  - So pointer will help the main function or program to access the heap area. Program can access heap only through the use of pointers.
    ![Code Section and Heap](https://i.imgur.com/EwTo0Bj.png)

- Another great reason for using pointers is, say we have a file on our disc and we want to access this file by a program, this can be done using a file pointer for accessing files. Accessing a network connect can also be done using a pointer indirectly. A code accesses only code section and stack directly rest of it us done via pointers as a proxy.

  - Whereas in languages such as C# and JAVA there are no pointers so these languages do not allow accessing devices through programs.JVM in JAVA or common language run-time or in .NET has to be used in case of C# to access these devices on a network and other components. There is no system programming possible using JAVA and C# but C and C++ have pointers and allows us to access devices, enabling us to do system programming, developing OSs, device drivers the only reason being this language has pointers.

## Declaration of Address/Pointer Variable :

Address variables have \* sign which makes them different from data variables when declared.

```c++
int *ptr ; // Can store the address of the data.
```

As ptr is also a variable but it is an address variable and it will occupy some space as well say it occupies 300/301 memory address.

If we say **`ptr = &x;`** Then the address variable ptr will store 200 address value and thus will point towards x. ptr has address of x and is pointing to x, showing the location of x. That's why it is called pointer.

```c++
int *ptr ; // Declaration of a pointer.
ptr = &x ; // Initialization of a pointer.
cout << x ; // Gives output as 10.
cout << &x ; // Gives 200, address of x.
cout << ptr ; // 200, address of x as we did ptr = &x above
cout << &ptr ; // Gives 300, address in memory for ptr.
cout << *ptr; // Displays the data stored at the memory address which ptr holds i.e. 10 Dereferencing
```

```c++
// Declaration of  a pointer using *
int *ptr;

// Initialization of a pointer : Feed in the address of variable to which you want ptr to point to
ptr = &x ;

// Dereferencing the pointer : Accessing the data stored at the memory location ptr holds as value
cout << *ptr ; // Will print the data of the memory address pointer is pointing to. In above example address 200 had the data 10.
```

- Size of memory required in the heap is decided during the runtime and not at compile time.

## MEMORY LEAK

- Say apart from main function we allocated a memory and function has stopped, taken some memory in heap we have set pointer to the array in heap as NULL before deallocating this memory then memory belongs to the program but program is not pointing to it as the only way to access it has been assigned NULL that is the address of that array in heap has been forgotten so we can't deallocate it neither can we use/access it in our program, it just sits there taking up space.

- If beforehand we assign p = NULL before deleting then we will lose track of the address which was assigned to array created by p and it will be there in memory even if we do not want the array as long as the program is running, this is memory leak.

- `nullptr` a built-in literal made only for pointer for newer version of C++.

- Only 5 arithmetic operations are allowed in pointers. Nothing else. let p and q are 2 pointers

  - p++
  - p--
  - p += n //n is an integer
  - p -= n //n is an integer
  - int i = q-p; //addresses of p and q can be subtracted showing how far they are from each other.
    - Let p is at 200 and q is at 206 and each int is assumed to be of 2 bytes so this means **q-p/2** gives us 3. That means q is 3 locations ahead in the array of the pointer p.
    - To find out how far apart 2 pointers are we subract pointer 1 address from pointer 2 address and divide the entire thing by the size of data type of the pointers.
    - (200-206)/3 means pointer 1 is nearer and pointer 2 is farther away as the answer comes out to be -3 on solving. If we get positive result that means first pointer is farther as compared to second pointer. Getting negative result means second pointer is far away.

- Due to wrong use of pointers systems or programs may crash not at the compile time but at the run time. We may get runtime errors when we use pointers in a wrong manner. Runtime errors are very dangerous due to the sheer fact that when we deliver our software to the client then it's on the reputation of firm or the freelance programmer who wrote the code. Getting error at the runtime is similar to a company selling a car whose compile time or in-factory tests showed no error but as soon as the client purchases the car and it is on road the at that moment suddenly there are problems on the user end.

## Errors with Pointers

- Due to wrong use of pointers systems or programs may crash not at the compile time but at the run time. We may get runtime errors when we use pointers in a wrong manner.

- Uninitialized Pointers: Always initialize pointers at declaration if using them, if we wanna initialize them later then initialize them with nullptr, then change later.

- Memory Leak
- Dangling Pointers

- A dangling pointer P points to the location which no longer belongs to the program. Here pointer was initialized but memory is deallocated and after that pointer is used to access that memory leading to error. These problems are caused due to negligence of beginner programmers. To avoid these kinds of mistakes and runtime failures java and .NET has removed the concept of pointers. Those languages are managed languages and JVM will try to deallocate the memory when it is not in use. That is the reason those languages are known as managed ones but the advantage of C++ is that it gives more power to the programmer.

- When a pointer is pointing at the memory address of a variable but after some time that variable is deleted from that memory location while the pointer is still pointing to it, then such a pointer is known as a **dangling pointer** and this problem is known as the dangling pointer problem.

- After delete we can do p = nullptr meaning pointer p is not pointing anywhere and this is correct way to do it.
- For pointers use nullptr literal and not NULL.

- Reference is nothing but a nickname of this variable, alias.
  ```cpp
  int x=10;
  int &y=x;
  ```
- So now x can be accessed using the name y too. So this leads to memory which we were initially calling as x can now be called y as well. We do not need this in same function.

- Reference doesn't consume any memory. Once we declare and initialize a reference we cannot make it a nickname for another variable. Reference is internal pointer. No symbol table entry.

## l-value and r-value

- variable on left of = is l-value, it means memory.
- variable on right of = is r-value, it means data.
  ```CPP
  int x = 10; // x is l-value and 10 r-value so this mean store value of 10 at address of x
  int y = x; // y is l-value and x is r-value so this mean store value of x at address of y
  ```

## Pointer to functions

- We know that we can have pointer to any primitive data type, we can also have pointer of type class.
- We can also have pointer to a function.

  - Syntax for declaration: `return_type (*function_pointer_name)(parameters_type); //Declaration`

    - eg. `int (*fp)(int, int);`
    - eg. `void (\*f)();`

  - Assigning the function to pointer: Equate it to fucntion name.

    - eg. `fp = max;`
    - eg. `f = display;`

  - Calling the function:
    - eg. `(*fp)(10,12); // return 12`
    - eg. `(*f)() // print Hello`

- On declaring a pointer to a function everything is same as prototype of a function, but instead of function name we have pointer name in bracket with parameters in another bracket.
- Initialization done using function name.
- Calling done by giving function pointer name inside () and pass required parameters if any.

- This is like polymorphism. In function over-riding internally functional pointers are used to achieve run-time polymorphism using function over-riding. One function pointer can point to any function with same signature/prototype.
