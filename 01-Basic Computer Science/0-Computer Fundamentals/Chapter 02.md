## 0 Boolean Logic and Logic Gates
- Computers have evolved from **electromechanical devices**, that often had decimal representations of numbers – like those represented by teeth on a gear to **electronic computers** with transistors that can turn the flow of electricity on or off.
- Binary means two states. 
	- 0 == false == Off == 0V
	- 1 == true == On == 5V
- Some early electronic computers were ternary, that's three states, and even quinary, using 5 states.	
	>**The problem is, the more intermediate states there are, the harder it is to keep them all seperate.**
- In Boolean Algebra, the values of variables are true and false, and the operations are logical.	
	- AND, OR, NOT, NAND, NOR, XOR, XNOR.
- A transistor is like a simple logic gate that does nothing, It's like buffer whaterver the input is the output is the same, but we can create other gates from different arrangements of transistors.
- `**So if we go down and clear the layer of abstraction we see, logics gates are nothing but Integrated Circuits of transistors, vaccum tubes and resistors.**`

## 1 The World of Binary
- The two states of binary are called `Bits`.
- 8-bits is such a common size in computing, it has a special word: a byte. 
- a kilobyte has two to the power of 10 bytes, or 1024.
- Computers must label locations in their memory, known as addresses, in order to store and retrieve values.
- Most computers use the first bit for the sign: 1 for negative, 0 for positive numbers, and then use the remaining bits for the number itself. `Storing Integers`
-  The standard to stores decimal values is sort of like scientific notation.
-  In a 32-bit floating point number, the first bit is used for the sign of the number. The next 8 bits are used to store the exponent and the remaining 23 bits are used to store the significand. `Storing Floating Point numbers`
-  ASCII was a 7-bit code, enough to store 128 different values. With this expanded range, it could encode capital letters, lowercase letters, digits 0 through 9, and symbols like the @ sign and punctuation marks. `Storing Characters`.
	-  Problem arrived when languages apart from english come into picture not 7-bit seemed. less 
-  This ability to universally exchange information is called `interoperability`.
-   `Unicode` – one format to rule all the characters.
	-   The most common version of Unicode uses 16 bits with space for over a million codes - enough for every single character from every language ever used.
-  File formats like MP3s or GIFs – use binary numbers to encode sounds or colors of a pixel in our photos, movies, and music.
-  `**So if we go down and clear the layer of abstraction we see, under the hood it all comes down to long sequences of bits. Text messages, videos, every webpage on the internet, and even your computer’s operating system, are nothing but long sequences of 1s and 0s.**`