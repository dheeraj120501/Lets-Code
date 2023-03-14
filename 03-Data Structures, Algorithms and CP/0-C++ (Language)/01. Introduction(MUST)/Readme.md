# Why C++ ?

1. It is widely used even today due to its large applications, as well as lots and lots of legacy code is also written on C++ already, so it is an integral part of many crucial systems we see today.
2. C++ follows Object Oriented Paradigm, lots of new languages are Object Oriented and it it provides lots of features in Object Oriented which are not available in newer languages and syntactically it is much better, even if that means you have to learn a lots of things due to sometimes exhaustive syntax. Which plays a crucial role in giving programmers more power and freedom over writing code in the way they want.
3. C++ is compatible with hardware due to it's nature of being a low level language which is easier for computers to understand. Proving to be a great choice for making Apps which run directly over the OS. So here is a layer of Hardware >> OS >> Application.
4. Looking at applications such as .Net, C#, Java or Python, these languages do not run directly over the OS but instead they need an interpreter that is a `run time environment` like java runs inside JVM and .NET programs run inside Common Language Run-time environment CLR.
   So, interpreter is used to establish interaction between OS and Hardware which makes it as follows (Hardware >> OS >> Environment >> App) due to this intermediate interference of environment layer these languages aren't that powerful compared to C++ which directly interacts with OS or hardware.
5. C++ is still pretty much the most used language when you need to write fast code that performs well or if you're writing for a weird architecture or a platform and you need the code to run natively, if you want direct control over Hardware C++ is for you.

## List of applications of C++

1. System Softwares/Tools
2. Embedded Systems (Microprocessors & Controllers viz. Arduino,Rasp)
3. Operating Systems, Interpreters
4. Platforms and Engines
5. Games & Graphics

We write our C++ code as text(just text) and then we need some way to transform that text into an actual application that our computer can run. In going from that text form to an actual executable binary we basically have two main operations that need to happen one of them is called compiling and other is called linking.

# How C++ works

We have a series of source files where we write actual code in and then it is passed through a compiler which compiles it into some kind of binary, now that binary can be some sort of library or it can be an actual executable program.

There are 3 steps to convert our cpp files to a binary (executable or library):

- Preprocessing (Compiler)
- Compiling (Compiler)
- Linking (Linker)

Once our preprocessor statements have been evaluated our file gets compiled, this is a stage where our compiler transforms all of the C++ code into actual machine code. There are several important settings that determine how this actually happens so let's take a brief look at them.

Each CPP file in our project gets compiled except header files, the header files get included via a preprocessor statement called `include` into a CPP file and that's when they get compiled. Every CPP file will get compiled into something called an **object file**(the extension for that using visual studios compiler is obj). Once we have all of the individual obj files which are the result of compiling the CPP files we need some way to stitch them together into one exe file and that's where linker comes in, it takes all the obj files and it glues them together, so the linker's job is to take all of our obj files and stitch them together into one exe file.

Every kind of symbol in C++ needs some kind of declaration, a declaration is exactly what it sounds like we're declaring that the thing declared exists now this is almost like a promise because we can just say "compiler there's a function called hogs" however the compiler will just believe us.

- The compiler doesn't care about resolving where that declared function actually is defined.
- When we build our entire project not just one file, once all our project files have been compiled the linker will actually find the definition of the declared function and wire it up to the declared function that we call here in main.cpp.
- If unable to find that definition it throws a linker error.

# How a C++ Compiler works

A C++ compiler actually needs to take our text files and convert them into an intermediate format called an object file.

Firstly it needs to pre-process our code which means that any preprocessor statements get evaluated then and there, once done it move on to tokenizing and pausing and basically sorting out the c++ language into a format that the compiler can actually understand, basically something called an **abstract syntax tree**.

- AST is a tree representation of the abstract syntactic structure of text (often source code) written in a formal language, the compilers job is to convert all of our code into either constant data or instructions. Once the compiler has created this abstract syntax tree it can begin actually generating code now this code is going to be the actual machine code that our CPU will execute.
- The AST is used intensively during semantic analysis, where the compiler checks for correct usage of the elements of the program and the language. The compiler also generates **symbol tables** based on the AST during semantic analysis. A complete traversal of the tree allows verification of the correctness of the program (check for syntax error).

Basic Preprocessor statements are #include, #define, #if-#endif.

- #include will go to the file copy it's entire content and paste it in the place where it is written.
  - #include <iostream> will copy the entire iostream file code in it's place.
- #define will search the entire file for the defined word and replace it with the word asked.
  - #define i int will find all the i in the file and replace them with int.
- #if-#endif will allow the function in it to work only if the condition is met.

# How a C++ Linker work

The primary focus of linking is to find where each symbol and function is and link them together.

The linker take all of our objects files that were generated during compilation and link them all together, it will also pull in any other libraries that we may be using like the C runtime library, the C++ standard library, our platform api if necessary etc.

There's also different types of linking like static linking and dynamic linking.

Putting `static` in front of a function means that the function is only declared for the translation unit in which it is written.

A **translation unit** is the basic unit of compilation in C++. It consists of the contents of a single source file, plus the contents of any header files directly or indirectly included by it, minus those lines that were ignored using conditional preprocessing statements.

- A single translation unit can be compiled into an object file, library, or executable program.
- The notion of a translation unit is most often mentioned in the contexts of the One Definition Rule, and templates.

C and C++ programs consist of one or more source files, each of which contains some of the text of the program. A source file, together with its include files (files that are included using the #include preprocessor directive) but not including sections of code removed by conditional-compilation directives such as #if, is called a **translation unit**.

- It is basically a file (.c/.cpp), after it's finished including all of the header files.

# Compiler

g++ command is a GNU C++ compiler invocation command, which is used for preprocessing, compilation(converting to assembly), assembly(assembly to object file) and linking of source code to generate an executable file.

The whole process is **source code -> assembly code -> object/machine code -> linking**.

The different **options** of g++ command allow us to stop this process at the intermediate stage.

- **-S** is used to only compile the file_name and not assembling or linking. It will generate a file_name.s assembly source file.
- **-c** is used to only compile and assemble the file_name and not link the object code to produce executable file. It will generate a file_name.o object code file in present working directory.
- **-o** compiles and links file_name and generates executable target file with target_name (or a.out by default).
- **-Wall** prints all warning messages that are generated during compilation of file_name.
- **-02** is to enable optimization of code.
- To let the compiler follow a specific C++ standard we use **-std=** option and give the standard like **-std=c++17**.

Compile and link multiple files: When -c flag is used, it invokes the compiler stage which translates source code to object code. When -o flag is used it links object code to create the executable file from file_name.o to a.out(default), multiples files may be passed together as arguments.

- eg. `g++ -c helloWorld.cpp hello.cpp` converts both the files in their respective object files or `g++ -o main.exe helloWorld.o hello.o` link both the object files and create one final main.exe file.

- There is no one way how C++ is implemented although the majority of contemporary C++ implementations follow the approach of compiler/linker and provide libraries as a collection of files with declarations and library files providing implementations of these declarations.

  - e.g. cling directly interprets C++ code without compiling.

- To give compiler vendors greater freedom, the C++ standards committee decided not to dictate the implementation of name mangling, exception handling, and other implementation-specific features(remember OpenGL and Khronoss group). The downside of this decision is that object code produced by different compilers is expected to be incompatible.

# Makefiles

Makefile is a program building tool which runs on Unix, Linux, and their flavors. It aids in simplifying building program executables that may need various modules. To determine how the modules need to be compiled or recompiled together, **make** takes the help of user-defined makefiles.

## Motivation

For a large project where we have thousands of source code files, it becomes difficult to maintain the binary builds.

Compiling the source code files can be tiring, especially when you have to include several source files and type the compiling command every time you need to compile. Makefiles are the solution to simplify this task.

Makefiles are special format files that help build and manage the projects automatically. The **make** command allows you to manage large programs or groups of programs.

## Make VS CMake

# How to approch a Problem

1. Identify and Understand the problem.
1. Find ways to solve it.
1. Select the best way.
1. Breakdown the best way into smaller subparts.
1. Write down the solution on paper.
1. Verify the solution using dry running.
1. Evaluate the solution.
1. Write the code.

# Data VS Information VS Knowledge

Data is unorganized facts and figures.

Information is organized, contextualized, categorized, calculated and condensed data.

Knowledge is our understanding and experience.

# Programming paradigms

The programming paradigm can be categorized into 2 broad categories imperative(Procedural, Structured or Object Oriented) and declarative(Functional, Logical).

Some common paradigms are like Procedural, Modular, Generic, Object-Oriented etc.

There are several kinds of major programming paradigms:

- **Imperative**: The imperative programming paradigm assumes that the computer can maintain through environments of variables any changes in a computation process.

  - Computations are performed through a guided sequence of steps, in which these variables are referred to or changed.
  - The order of the steps is crucial, because a given step will have different consequences depending on the current values of variables when the step is executed.
  - We have to tell the computer each step to in order to make the thing work.
  - This way is efficient, close to the machine and usually programmers gets familiar to it and so it's popular.
  - The problem with this is side effects also make debugging harder, abstration is more limitted than with some paradigms, order is crucial, which doesn't always suit itself to problems.

- **Logical/Declarative**: The Logical Paradigm takes a declarative approach to problem-solving. Various logical assertions about a situation are made, establishing all known facts. Then queries are made.

  - The role of the computer becomes maintaining data and logical deduction.

- **Functional**: The Functional Programming paradigm views all subprograms as functions in the mathematical sense-informally, they take in arguments and return a single solution.

  - The solution returned is based entirely on the input, and the time at which a function is called has no relevance.
  - The computational model is therefore one of function application and reduction.

- **Object-Oriented**: Object Oriented Programming (OOP) is a paradigm in which real-world objects are each viewed as seperate entities having their own state which is modified only by built in procedures, called methods.

  - Because objects operate independently, they are encapsulated into modules which contain both local environments and methods. Communication with an object is done by message passing.
  - Objects are organized into classes, from which they inherit methods and equivalent variables. The object-oriented paradigm provides key benefits of reusable code and code extensibility.

# Data structures and ADT

A mathematical model on a particular way of storing and organizing data(data structure) with their operations are called Abstract Data Types (ADTs). An ADT consists of two parts:

1. Declaration of data
2. Declaration of operations

While defining the ADTs do not worry about the implementation details.

- ADT only tells us about the `WHAT` of the operations and not the `HOW`, basiaclly it tells what the operation is supposed to do and not how it is to be done.

Commonly used ADTs include: Linked Lists, Stacks, Queues, Priority Queues, Binary Trees, Dictionaries, Disjoint Sets, Hash Tables, Graphs, and many others.

Data structure is the physical implementation of ADT.

General data structure types include arrays, files, linked lists, stacks, queues, trees, graphs and so on.

Data structure can be Linear or Non-Linear(Based on how data is stored in them), Static or Dynamic(Based on how memory is allocated to them), Persistant or Ephimeral.

Whenever we encounter any data structure we must try to answer 2 questions:

- How data is stored
- What operations does the DS provide

# Algorithm, Pseudocode and Flowchart

An algorithm is the step-by-step unambiguous instructions to solve a given problem.

In the traditional study of algorithms, there are two main criteria for judging the merits of algorithms: correctness (does the algorithm give solution to the problem in a finite number of steps?) and efficiency (how much resources (in terms of memory and time) does it take to execute the).

Chosing the effective algorithm can be done based on running time(TIME COMPLEXITY) and based on memory used(SPACE COMPLEXITY).

High level description of an algorithm is called **Pseudocode**.

- English para < Pseudocode < Program.

**Flowchart** is a diagram that depicts a process system or computer algorithm.

## Heuristic VS Algorithms

Heuristic, in a nutshell is an "Educated guess".
