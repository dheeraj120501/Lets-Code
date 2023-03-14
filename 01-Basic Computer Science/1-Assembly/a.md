Computer programs can be thought of as a long strip of instructions that are loaded into memory and divided up into sections (or segments). This general pool of memory is shared between all programs and can be used to store variables, instructions, other programs or anything really. Each segment is given an address so that information stored in that section can be found later.

To execute a program that is loaded in memory, we use the global label \_start: to tell the operating system where in memory our program can be found and executed. Memory is then accessed sequentially following the program logic which determines the next address to be accessed. The kernel jumps to that address in memory and executes it.

It's important to tell the operating system exactly where it should begin execution and where it should stop.

the program continued sequentially executing the next address in memory, which could have been anything. We don't know what the kernel tried to execute but it caused it to choke and terminate the process for us instead - leaving us the error message of 'Segmentation fault'. Calling sys_exit at the end of all our programs will mean the kernel knows exactly when to terminate the process and return memory back to the general pool thus avoiding an error.

sys_write requires that we pass it a pointer to the string we want to output in memory and the length in bytes we want to print out. If we were to modify our message string we would have to update the length in bytes that we pass to sys_write as well, otherwise it will not print correctly.

As we won't know the length of the data when we compile our program, we will need a way to calculate the length at runtime in order to successfully print it out.

To calculate the length of the string we will use a technique called pointer arithmetic. Two registers are initialised pointing to the same address in memory. One register (in this case EAX) will be incremented forward one byte for each character in the output string until we reach the end of the string. The original pointer will then be subtracted from EAX. This is effectively like subtraction between two arrays and the result yields the number of elements between the two addresses. This result is then passed to sys_write replacing our hard coded count.

The CMP instruction compares the left hand side against the right hand side and sets a number of flags that are used for program flow.

Subroutines are functions. They are reusable pieces of code that can be called by your program to perform various repeatable tasks. Subroutines are declared using labels just like we've used before (eg. \_start:) however we don't use the JMP instruction to get to them - instead we use a new instruction CALL. We also don't use the JMP instruction to return to our program after we have run the function. To return to our program from a subroutine we use the instruction RET instead.

The great thing about writing a subroutine is that we can reuse it. If we want to be able to use the subroutine from anywhere in the code we would have to write some logic to determine where in the code we had jumped from and where we should jump back to. This would litter our code with unwanted labels. If we use CALL and RET however, assembly handles this problem for us using something called the stack.

The stack is a special type of memory. It's the same type of memory that we've used before however it's special in how it is used by our program. The stack is what is call Last In First Out memory (LIFO).

You can store a lot of things on the stack such as variables, addresses or other programs. We need to use the stack when we call subroutines to temporarily store values that will be restored later.

Any register that your function needs to use should have it's current value put on the stack for safe keeping using the PUSH instruction. Then after the function has finished it's logic, these registers can have their original values restored using the POP instruction. This means that any values in the registers will be the same before and after you've called your function. If we take care of this in our subroutine we can call functions without worrying about what changes they're making to our registers.

The CALL and RET instructions also use the stack. When you CALL a subroutine, the address you called it from in your program is pushed onto the stack. This address is then popped off the stack by RET and the program jumps back to that place in your code. This is why you should always JMP to labels but you should CALL functions.

External include files allow us to move code from our program and put it into separate files. This technique is useful for writing clean, easy to maintain programs.

Reusable bits of code can be written as subroutines and stored in separate files called libraries. When you need a piece of logic you can include the file in your program and use it as if they are part of the same file.

In assembly, variables are stored one after another in memory so the last byte of our msg1 variable is right next to the first byte of our msg2 variable. We know our string length calculation is looking for a zero byte so unless our msg2 variable starts with a zero byte it keeps counting as if it's the same string (and as far as assembly is concerned it is the same string). So we need to put a zero byte or 0h after our strings to let assembly know where to stop counting.

Note: In programming 0h denotes a null byte and a null byte after a string tells assembly where it ends in memory.

Linefeeds are essential to console programs like our 'hello world' program. They become even more important once we start building programs that require user input. But linefeeds can be a pain to maintain. Sometimes you will want to include them in your strings and sometimes you will want to remove them.

A call to sys_write requires we pass a pointer to an address in memory of the string we want to print so we can't just pass a linefeed character (0Ah) to our print function. We also don't want to create another variable just to hold a linefeed character so we will instead use the stack.

When you push items onto the stack, ESP is decremented to point to the address in memory of the last item and so it can be used to access that item directly from the stack.

Since ESP points to an address in memory of a character, sys_write will be able to use it to print.

NOTE: Oah is line feed or new line character and Oh is null terminating byte.

Passing arguments to your program from the command line is as easy as popping them off the stack in NASM. When we run our program, any passed arguments are loaded onto the stack in reverse order. The name of the program is then loaded onto the stack and lastly the total number of arguments is loaded onto the stack. The last two stack items for a NASM compiled program are always the name of the program and the number of passed arguments.

BSS stands for Block Started by Symbol. It is an area in our program that is used to reserve space in memory for uninitialised variables. We will use it to reserve some space in memory to hold our user input since we don't know how many bytes we'll need to store.

When sys_read detects a linefeed, control returns to the program and the users input is located at the memory address you passed.

Counting by numbers is not as straight forward as you would think in assembly. Firstly we need to pass sys_write an address in memory so we can't just load our register with a number and call our print function. Secondly, numbers and strings are very different things in assembly. Strings are represented by what are called ASCII values. ASCII stands for American Standard Code for Information Interchange.
Remember, we can't print a number - we have to print a string. In order to count to 10 we will need to convert our numbers from standard integers to their ASCII string representations.

We achieve this by passing the number in EAX. We then initialise a counter in ECX. We will repeatedly divide the number by 10 and each time convert the remainder to a string by adding 48. We will then push this onto the stack for later use. Once we can no longer divide the number by 10 we will enter our second loop. In this print loop we will print the now converted string representations from the stack and pop them off. Popping them off the stack moves ESP forward to the next item on the stack. Each time we print a value we will decrease our counter ECX. Once all numbers have been converted and printed we will return to our program.

Namespace is a necessary construct in any software project that involves a codebase that is larger than a few simple functions. Namespace provides scope to your identifiers and allows you to reuse naming conventions to make your code more readable and maintainable. In assembly language where subroutines are identified by global labels, namespace can be achieved by using local labels.

Local labels are prepended with a "." at the beginning of their name for example ".finished". A local label is given the namespace of the first global label above it. You can jump to a local label by using the JMP instruction and the compiler will calculate which local label you are referencing by determining in what scope (based on the above global labels) the instruction was called.

The EXEC family of functions replace the currently running process with a new process, that executes the command you specified when calling it.

The naming convention used for this family of functions is exec (execute) followed by one or more of the following letters.
E - An array of pointers to environment variables is explicitly passed to the new process image.
L - Command-line arguments are passed individually to the function.
P - Uses the PATH environment variable to find the file named in the path argument to be executed.
V - Command-line arguments are passed to the function as an array of pointers.
