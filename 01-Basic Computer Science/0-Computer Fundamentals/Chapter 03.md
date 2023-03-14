## 0 ALU (Computer starts calculating)
-   The ALU is the mathematical brain of a computer.
-   The `Intel 74181` released in 1970, it was the first complete ALU that fit entirely inside of a single chip, but can do operation on 4 bit inputs.
-   An ALU is really two units in one -- there’s an arithmetic unit and a logic unit.
-   Let's talk about Arithematic unit and the most basic operation in that unit.
	- `Half adders` are used to add 2 bits and output `sum(A XOR B)` and `carry(A AND B)`.
		> Half adders can only add 2 single bit :( 
	- `Full adders` are used to add 3 bits and output `sum(A XOR B XOR C)` and `carry((A AND B) OR (B AND C) OR (A AND C))`.
		> Full adders can only add 3 single bit not bit string.
	- Using these Full adders we create a `8 bit ripple carry adder`.
	- An `overflow` occurs when the result of an addition is too large to be represented by the number of bits you are using. So if we want to avoid overflows, we can extend our circuit with more full adders, allowing us to add 16 or 32 bit numbers. An additional downside is that it takes a little bit of time for each of the carries to ripple forward.
	- Modern computers use a slightly different adding circuit called a `carry-look-ahead`adder which is faster, but ultimately does exactly the same thing-- adds binary numbers.
	- Some basic operations are: `ADD`, `ADD with CARRY`, `SUBTRACT`, `SUBTRACT with BORROW`, `NEGATE`, `INCREMENT`, `DECREMENT`, `PASS THROUGH`
	- There are no multiply and divide operations as simple ALU don't have ckt for this instead **multiply is addition in loops**and **division is subtraction in loops**, this is how many simple processors, like those in our thermostat, TV remote, and microwave, do multiplication.
	- **In smartphones and computers we have ckt dedicated for them as well.**
- The other unit i.e. `LOGICAL UNIT` just do logical operations and checks.
- ALUs also output a series of Flags, which are 1-bit outputs for particular states and statuses.
- `So this layer of abstraction mean the ALU contains different ckts of the logic gates that make it do operations.`

##  1 Computer starts remembering things (Memory)
- The `AND-OR Latch` has two inputs, a "set" input, which sets the output to a 1, and a "reset" input, which resets the output to a 0. If set and reset are both 0, the circuit just outputs whatever was last put in it. It remembers a single bit of information! Memory! This is called a `latch` because it “latches onto” a particular value and stays that way.
- The action of putting data into memory is called writing, whereas getting the data out is called reading.
- `A latch can only store one bit`, so If we put 8 latches side-by-side, we can store 8 bits of information like an 8-bit number.
- A group of latches operating to store a bit string is called a `register`, which holds a single number, and the number of bits in a register is called `width of register`.
- Early computers had 8-bit registers, then 16, 32, and today, many computers have registers that are 64-bits wide.
- Now arranging latches side by side can require a lots of wires, The solution is a `matrix`, for 256 bits, we need a 16 by 16 grid of latches with 16 rows and columns of wires. To activate any one latch, we must turn on the corresponding row and column wire.
- To convert from an address into something that selects the right row or column, we need a special component called a `multiplexer`.
- Now by bundling these little little memory we create big memory, To store address of a gigabyte – or a billion bytes of memory – we need 32-bit addresses or 4 bytes address. An important property of this memory is that we can access any memory location, at any time, and in a random order. For this reason, it’s called Random-Access Memory or RAM.
- SRAM - Static Random-Access Memory, uses latches. There are other types of RAM, such as DRAM, Flash memory, and NVRAM. These are very similar in function to SRAM, but use different circuits to store the individual bits -- for example, using different logic gates, capacitors, charge traps, or memristors.
- `So fundamentally, all of memory technologies store bits of information in massively nested matrices of memory cells.`

## 2 Central Processing Unit
- A CPU’s job is to execute programs (set of instructions).
- If these are mathematical instructions, like add or subtract, the CPU will configure its ALU to do the mathematical operation. Or it might be a memory instruction, in which case the CPU will talk with memory to read and write values.