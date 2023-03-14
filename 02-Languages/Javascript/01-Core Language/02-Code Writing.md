## 0
- Debugging is the process of finding and fixing errors within a script.
- It also allows to trace the code step by step to see what exactly is going on.
- Every IDE and most browsers contain various debugging tools.
- In chrome the one is in the Source tab where we can open any file can use the debugg tools there.
- Sometimes we just use console to find error by printing.
- A `breakpoint` is a point of code where the debugger will automatically pause the JavaScript execution.
- `Conditional breakpoint`, only triggers when the given expression is truthy.
- We can also pause the code by using the `debugger;` command in it.


## 1
- There are some basic coding rules, not the must but are used widely:
  - No space between the function name and parentheses between the parentheses and the parameter.
  - A space between parameters.
  - Curly brace `{` on the same line, after a space.
  - Spaces around operators.
  - Indentation 2 spaces for content inside `{}`.
  - A semicolon `;` is mandatory.
  - A space after and before loops, conditionals. 
    eg. `if ()`, `for ()` 
  - A space between arguments.
  - An empty line between logical blocks.
  - Lines are not very long.
  - `} else {` without a line break.
  - Spaces around a nested call.
  - Try to avoid nesting code too many levels deep.
- A style guide contains general rules about **how to write code**, e.g. which quotes to use, how many spaces to indent, the maximal line length, etc. A lot of minor things.
- `Linters` are tools that can automatically check the style of your code and make improving suggestions.

## 2
- Comments are for documentation.
- `If the code is so unclear that it requires a comment, then maybe it should be rewritten instead`
- Explanatory comments are usually bad, SO...
  - Provide a high-level overview of components, how they interact, what’s the control flow in various situations, Just the interface (what) not the implementation (how).
  - Document function parameters and usage, like docstring.
  ```javascript
    /**
   * Returns x raised to the n-th power.
   *
   * @param {number} x The number to raise.
   * @param {number} n The power, must be a natural number.
   * @return {number} x raised to the n-th power.
   */
  ```
- Comments that explain the solution are very important. They help to continue development the right way.
- If the code has anything subtle and counter-intuitive, it’s definitely worth commenting.
- Ask these questions to yourself while commenting
  > Why are we coding this in the manner we are?
  > How does this code or function fit into the bigger picture of our code architecture?
  > Were there any "gotchas" or pitfalls we discovered as we wrote the code?
  > Is there anything important about this code that we might forget between now and when we revisit it later, that isn't obvious by reading the code?


## 3
- When testing a code by manual re-runs, it’s easy to miss something.
- Automated testing means that tests are written separately, in addition to the code. They run our functions in various ways and compare results with the expected.
- BDD is three things in one: tests AND documentation AND examples.
- Before creating the code of any function, we can imagine what the function should do and describe it. Such description is called a `specification` or, in short, a `spec`, and contains descriptions of use cases together with tests for them.
