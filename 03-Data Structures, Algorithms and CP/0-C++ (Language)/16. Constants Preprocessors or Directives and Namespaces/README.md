## Constants

- **Const:** It is a qualifier in C++ which is used at many places. Const stands for constant. Say we declare a variable x of value 10, and in memory it is present at location 200. We can do x++ and 10 becomes 11. `const int x = 10;`, now what this means is x is now a constant identifier and it is not a variable. You can't do anything such as modification of the value of const identifier. It is somewhat like `#define x 10` we looked at earlier.

- **#define x 10**: Now this is a preprocessor directive and it happens before the compilation, but `const int x = 10;`, consumes the memory of integer and can't be modified. If you have global constants you can use preprocessor directive like this, otherwise for local constants use constant identifier.

- **Pointers:**

```cpp
int main()
{
    int x = 10;
    int *ptr = &x; // ptr = 200 and *ptr = 10
    ++*ptr; // x = 10 --> x = 11
    cout<<*ptr; // Output 11
}
```

- **Constant Pointers**:

```cpp
int main()
{
    int x = 10;
    const int *ptr = &x; // ptr = 200 and *ptr = 10, read as pointer to an integer constant
    ++*ptr; // x = 10 --> ++*ptr Error as ptr is pointer to a constant
    cout<<*ptr; // Output 10 --> No error as const int pointer has read only access to x
    int y;
    ptr = &y; // Even though it was const ptr it can change the variable to which it is pointing to.
    cout << *ptr; //This will not give any errors but as the pointer is const int type it can't be used to do ++*ptr;
}
```

- Another way of using pointers where pointer is constant and not the data to which it is pointing

```cpp
int main()
{
    int x = 10;
    int *const ptr = &x; // constant pointer to an integer. Nor the data nor the int is constant here but ptr is constant here. ptr can't be modified to point to some other address than the one it is assigned to.
    int y;
    ptr = &y; // Can't be done. will give ERROR!
    ++*ptr; // This can be done as we increment the value and it is not constant in this case.

}
```

- Constant pointer to an integer constant: Can't be pointed to any other variable, neither it can modify the value of the variable it is pointing to.

```cpp
int main()
{
    int x = 10;
    const int *const ptr = &x; // constant pointer to an integer constant. Nor the data nor the int is constant here but ptr is constant here. ptr can't be modified to point to some other address than the one it is assigned to.
    int y;
    ptr = &y; // Can't be done. will give ERROR!
    ++*ptr; // This cannot be done as we  increment the value and it is not constant in this case.
}
```

- **Constant keyword in functions**

```cpp
class Demo
{
    public:
        int x = 10;
        int y = 20;

        void display() const{
            x++;
            cout<< x << " " << y << endl;
        }
};

int main()
{
    Demo d;
    d.Display(); // x --> 11 and y --> 20 will be displayed.
}
```

- If you do not want the member function of a class to modify the member, in that case we can write const as above just after the function name, inside the prototype of the function. Compiler will restrict the member function from doing modification of any kind to the data members. This is useful when you are sure that there is no need for a particular function in a class to modify the members of the class, so that even if by mistake due to some logical error, compiler will be there to the rescue and will notify when member function marked with const tries to modify some member's data.

- **Working with functions and call by reference** : Just add const in the function prototype and you won't have your member function modifying class member values.

```cpp
void fun(const int &x,int &y)
{
    x++;
    int << x << " "<< y;
}

int main()
{
    int a = 10,b = 20;
    fun(a,b);
}
```

## Preprocessor Directives/

- **Preprocessor Directives**: These are the instructions to compiler. We give some instructions to the compiler before it starts compiling the program, compiler can follow and perform those instructions. An example of this is `#define` preprocessor directive, used often at times to define a constant value. Using `#define` what we define are known as symbolic constants.

  - NOTE: Anything beginning with `#` is a preprocessor directive, the first thing that a compiler does is it preprocesses the preprocessor statements.
  - There are 4 main types of preprocessor directives:
    - Macros(#define)
    - File Inclusion(#include)
    - Conditional Compilation(#if - #endif)
    - Other directives

```cpp
#include <iostream>
using namespace std;
#define PI 3.14
#define c cout
int main()
{
    c<<pi; // pi will output 3.14 and c will translate to cout
}
```

- Using `#define` we can even write functions.
  - The # and ## preprocessor operators are available in C++ and ANSI/ISO C for macro function. The # operator causes a replacement-text token to be converted to a string surrounded by quotes while ## operator is used to concatenate two tokens.

```cpp
#include <iostream>
using namespace std;
#define MIN(a,b) (((a)<(b)) ? a : b)
#define SQR(x) (x * x) // Print square of integer passed
#define MSG(x) #x // Will print whatever is passed to MSG as string i.e. enclosed in double quotes.
#define CONCAT( x, y )  x ## y // This will add x and y
int main()
{
    cout << SQR(5); // Will give 25 as output.
}
```

- C++ provides a number of predefined macros like \_\_LINE\_\_, \_\_FILE\_\_, \_\_DATE\_\_, \_\_TIME\_\_\_ etc.

- The #include includes the entire file in place of the directive it basically copies the entire code and paste it in place the include statement.

- Basic conditional preprocessor directive are of type:
  - ```cpp
    #ifdef macro_name
    statement1;
    statement2;
    .
    .
    statementN;
    #endif
    ```
  - ```cpp
    #ifndef macro_name
    statement1;
    statement2;
    .
    .
    statementN;
    #endif
    ```
  - ```cpp
    #if booleanExpression
    statement1;
    statement2;
    .
    .
    statementN;
    #endif
    ```
- If condition with preprocessor directives so that if not defined something, only then we will define something as a macro in the following way:

```cpp
#include <iostream>
using namespace std;

#ifndef PI
    #def PI 3.14
#endif

int main()
{
    cout << PI;
}
```

- Some other directives include:
  - `#undef` Directive: The #undef directive is used to undefine an existing macro.
  - #pragma Directive: This directive is a special purpose directive and is used to turn on or off some features. This type of directives are compiler-specific, i.e., they vary from compiler to compiler.

## Namespaces

- **Namespaces**: These are used to remove name conflict from the program. If you are writing multiple functions with the same name, not overloaded but independent functions not part of any class, signature and everything is same, and we have multiple classes having same name, in that case there will be name conflict, so we can put the 2 functions with same name inside namespaces in the following manner.
- They are used to declare scopes.

```cpp
#include <iostream>
using namespace std;
namespace First //encapsulating within namespaces
{
    void func()
    {
        cout<<"First";
    }
}

namespace Second
{
    void func()
    {
        cout<<"Second";
    }
}
int main()
{
    First::func();
    // if you do using namespace First in that case every time you call func() First::func() would be called by default and you can do Second::func() where ever you want Second
    // std namespace has cin, cout in it that is why we have been writing using namespace std.
    return 0;
}
```

- If we don't want to use `::` operator with namespace name we can tell the compiler what namespace we are using. This will include the entire namespace but might again cause conflicts. So using `::` is the prefered way.

  ```cpp
  using namespace std;
  using namespace Second;
  ```

- Using statements (including using declarations and using directives) can be used to avoid having to qualify identifiers with an explicit namespace. These should generally be avoided.
