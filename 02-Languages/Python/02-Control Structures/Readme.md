## Conditional Branching

- Conditional Branching is the ability of the software (program) to make the system execute one set of statements and skip the other, or vice versa.

- Python supports implementation of conditional branching using the if, elif and else statements.
- Switch is not available in python.

- Python interpreter always evaluates the criteria associated with an if statement and results in a boolean value.
- When the boolean result is true then the block of code associated with the if statement executes, otherwise not.

- It is important to know that else statement is optionally associated with an if or an elif statement.
  - \> is a comparison operator. It compares the LHS value being greater than RHS value and returns a boolean.
  - < is a comparison operator. It compares the LHS value being less than RHS value and returns a boolean.
  - == is a comparison operator. It compares the LHS and RHS values for equality and returns a boolean.

## Logical Operators

- and, or, not
- and / or are used for merging conditions

  1. Python gives higher priority to "logical and" as compared to "logical or".
  2. Python applies a short circuit behaviour that skips the evaluation of the RHS condition when:
     - LHS of `and` is false
     - LHS of `or` is true

- One liner if-else or Ternary operator of Python:
  - `statement if(condition) else statement`
  - Use them if they are one liners
