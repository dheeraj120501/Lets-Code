# Loops

Loops are iterative statements. As long as the condition is correct the code inside the block {} will continue to run.

There are 4 types of loops in C++ :

1. While loop :

   ```c++
   while (condition){
       statements to be executes
           if the condition is true
   }
   ```

2. do while loop : Ideal for case when you want program to run atleast once.

   ```c++
   do{
       set of conditions to be executed first (atleast once)
   }
   while(condition to check for){
   	repeats the stuff inside do
           if condition matches
   }
   ```

3. for loop : Needs initialization, condition, updation parameters to work. First initializer is executed, then condition is checked , on matching body below is executed and then updation is done, then again condition is checked and then body is executed.

   ```c++
   for(initialize, condition to check, update the initializer)
   {
       set of conditions to be executed
   }
   ```

4. Range based loops: To itterate over items of a collection directly.

```c++
   for (type x : collection/array){
       useful for accessing all the elements of an array.
   }
```

- If you have a number of iteration then go for _for loop_, if you don't know then _while_ or _do-while loop_.

## for_each loop

- For each loop are used to loop using iterators and a callback that will run for each element.
  ```cpp
    for_each(start_itr, end_itr, callbackFn);
  ```

## Infinite Loops

- for(;;){}
- while(1){}

## Working with digits

- if n is an integer
  - to get digits from last => n%10 (to get digit) and then do n /= 10 (for next iteration)
  - to get digits from start => (n/pow(10,dig-1))%10 and then dig--
  - to add dig x at the end of n => n\*10+x
  - to add dig x at the start of n => x\*pow(10,dig)+n

## Control Flow

- It is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated.
- This can be managed by `break`, `continue`, `goto`, `return` keywords.
- break and continue is to get out from a single loop.
- return is to get out from the function.
- goto is to get to a certain place in case of nested loops using labels.

- These control flow statements basically form the basis of how your flow goes. To understand loops and if statements and all of these control flow statements that is essentially the logic of programming.
  - These are the tools you have access to control the flow of your program basically which line gets executed next.
  - These tools are the only thing that can modify the behavior of your program.
