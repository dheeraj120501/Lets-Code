- By default the end character in python print() is /n. We can change it to something else by using end.
  - eg. print("Hello world",end=" ") // ends the space and not with \n
- We can also cascade so that we can print variables and String literals using ,(comma) operator.

- Python provides 2 loops:

  - for: To iterate through items of data structures or a range of values.
  - while: To iterate till the condition is met.

  - NOTE: with loops come some important keywords and functions like:
    1. in
    2. not in
    3. range(start,end,step) // end is excluded in iteration, default start is 0

## Control statement

- break : To stop loop
- continue : To move to next iteration

- NOTE: break and while must be used in a if-else block otherwise it doesn't make any sense.

## Some important number tricks:

- Fetch the last digit of a number
  - last_digit = number % 10
- Append the last digit to a number
  - number = number\* 10 + last_digit
- Eliminate the last digit of a number

  - number = number // 10

- `for-else` loop is just a normal loop whose else block will run iff for loop ended properly i.e. without break.
  - The loop can have break but if it ended due to break then else will not be executed.
