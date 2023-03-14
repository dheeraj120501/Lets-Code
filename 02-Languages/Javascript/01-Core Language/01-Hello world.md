## 0

- We can use a `<script>` tag to add JavaScript code to a page.
- The type and language attributes are not required.
- A script in an external file can be inserted with `<script src="path/to/script.js"></script>`.
- As a rule, only the simplest scripts are put into HTML. More complex ones reside in separate files.
- The benefit of a separate file is that the browser will download it and **store it in its cache**, other pages that reference the same script will take it from the cache instead of downloading it, so the file is actually downloaded only once, this reduces traffic and makes pages faster.
- If src is set, the script content (content inside the script tag) is ignored.

## 1

- Statements are syntax constructs and commands that perform actions.
  ```javascript
  alert("Hello");
  alert("World");
  ```
- Statements can be separated with a semicolon (optional).
- A semicolon may be omitted in most cases when a line break exists, JavaScript interprets the line break as an “implicit” semicolon. This is called an `automatic semicolon insertion`.
- In most cases, a newline implies a semicolon. But “in most cases” does not mean “always”! Thus it's recommend putting semicolons between statements even if they are separated by newlines. This rule is widely adopted by the community.

- One-line comments start with two forward slash characters //.
- Multiline comments start with a forward slash and an asterisk /_ and end with an asterisk and a forward slash _/.
- Nested comments are not supported!
  - There may not be /_..._/ inside another /_..._/. Such code will die with an error:

## 2

- `"use strict"` or `'use strict'`, when used in any Execution context (function) of a script, that Execution context (function) of script works the “modern” way. If used in the top Global Execution context, the whole script work modern way.
- Scoping in JS is done using {}, except in case of objects.
- Modern JavaScript supports “classes” and “modules” – advanced language structures (we’ll surely get to them), that enable use strict automatically.

## 3

- A variable is a “named storage” for data.
- Variable declaration and assignment.
- Declaration is done using `let`, `const`, `var` and assignment is done using `=`.
- A variable should be declared only once. A repeated declaration of the same variable is an error (in strict mode or with modern declaration tool let,const not with var).
- Naming a variable:
  - The name must contain only letters, digits, or the symbols $ and \_.
  - The first character must not be a digit.
- `Case matters and Non-Latin letters are allowed, but not recommended`
- There is a widespread practice to use constants as aliases for difficult-to-remember values that are known prior to execution. Such constants are named using capital letters and underscores. Capital-named constants are only used as aliases for “hard-coded” values.
- Don't use keywords to name variables it's not allowed.

## 4

- JavaScript, are called “dynamically typed”, meaning that there exist data types, but variables are not bound to any of them. Any var can store any type of value at any time.
  - `Value has type not variable`
- There are eight basic data types in JavaScript:
  - Number
  - BigInt
  - String
  - Boolean
  - Null
  - Undefined
  - Object
  - Symbol
- `typeof` operator returns the type of the argument.
  - As an operator: `typeof x`.
  - As a function: `typeof(x)`.
  - The result of typeof null is "object". That’s an officially recognized error in typeof behavior, coming from the early days of JavaScript and kept for compatibility. Definitely, null is not an object. It is a special value with a separate type of its own.
  - There’s no special “function” type in JavaScript. Functions belong to the object type. But typeof treats them differently, returning "function".
- Special numeric values
  - `Infinity` represents the mathematical Infinity ∞. It is a special value that’s greater than any number.
  - `NaN` represents a computational error. It is a result of an incorrect or an undefined mathematical operation. NaN is sticky. Any further operation on NaN returns NaN.
  - `-Infinity` is a special value that’s smaller than any number.
- Doing maths is “safe” in JavaScript. We can do anything: divide by zero, treat non-numeric strings as numbers, etc. The script will never stop with a fatal error (“die”). At worst, we’ll get NaN as the result.
- JS don't have characters.

## 5

- Tools to interact with user through browser:
  - `alert(mgs)` It shows a message and waits for the user to press “OK”.
    - The call to alert does not return a value. Or, in other words, it returns undefined.
  - `prompt(title, default)` It shows a modal window with a text message, an input field for the visitor, and the buttons OK(return input)/Cancel(return null).
    - prompt accept 2 arguments: The text to show the visitor, and an optional second parameter, the initial value for the input field.
  - `confirm()` The function confirm shows a modal window with a question and two buttons: OK(return true) and Cancel(return false).
- Limitations with these interaction:
  - The exact location of the modal window is determined by the browser. Usually, it’s in the center.
  - The exact look of the window also depends on the browser. We can’t modify it.
- `alert` is for output, `prompt` is for input and `confirm` is for confirmation.

## 6

- Most of the time, operators and functions automatically convert the values given to them to the right type, this is called type coersion.
- We can also change the type of value explicitly this is called type conversion.
  - The three most widely used type conversions are to string, to number, and to boolean.
    - `String(value)` This is string conversion, the conversion to string is usually obvious for primitive values.
    - `Number(value)` There are some rules in this conversion
      - `undefined` become `NaN`
      - `null` become `0`
      - `true/false` become `1/0`
      - `string` is read “as is”, whitespaces from both sides are ignored. An `empty string` becomes `0`. An `error` gives `NaN`.
    - `Boolean(value)`
      - `0`, `null`, `undefined`, `NaN`, `""` become `false` (falsy value), any other value is `true`.
      - `"0"` and space-only strings like `" "` are `true` as a boolean

## 7

- Operand and operator, operator can be unary, binary, ternary etc.
- Arithematic Operators are: `+` `-` `*` `/` `%` `**`.
- String concatenation: the plus operator + sums numbers but, if the binary + is applied to strings, it merges (concatenates) them.
  > Note that if any of the operands is a string, then the other one is converted to a string too.
- The binary `+` is the only operator that supports strings in such a way. Other arithmetic operators work only with numbers and always convert their operands to numbers.
- unary `+` does the same thing as Number(...), but is shorter.

  ```javascript
  // No effect on numbers
  let x = 1;
  alert(+x); // 1

  let y = -2;
  alert(+y); // -2

  // Converts non-numbers
  alert(+true); // 1
  alert(+""); // 0
  ```

- **Remember about precedence and associativity**
- An assignment `=` operator has a very low priority of 3. It assigns r-value to l-value(address) and return the assigned value.
  > All operators in JavaScript return a value.
- An interesting feature is the ability to chain assignments.
  ```javascript
  a = b = c = 10;
  ```
  - This assign 10 to c then return 10 which is assigned to b then the returned 10 is assigned to a.
- Other operators are `+=` `-=` `*=` `/=` `%=` `**=` `++` `--`
- Increment/decrement can only be applied to variables. Trying to use it on a value like 5++ will give an error.
- The operators ++/-- can be used inside expressions as well. Their precedence is higher than most other arithmetical operations.
- Bitwise Operator: Bitwise operators treat arguments as 32-bit integer numbers and work on the level of their binary representation.
  - `&` `|` `~` `^` `>>` `<<` `>>>`
- the comma operator `,` has very low precedence, lower than `=` it’s used to write shorter code.
  - The comma operator allows us to evaluate several expressions, dividing them with a comma `,`. Each of them is evaluated but only the result of the last one is returned.
  - Comma is a very sensitive operator so while using always make sure you use parenthesis, without parenthesis it gives the first and ignores the rest
    ```javascript
    alert(a=1,b=4,c=a*b)  \\1 no parenthesis so return a=1 and ignored rest.
    alert((a=1,b=4,c=a*b))  \\4 returned value of (a=1,b=4,c=a*b) which is c=a*b (the last result)
    ```

## 8

- Comparision operators `>` `<` `>=` `<=` `==` `===` `!=` `!==`, they return either `true` or `false`
- `String Comparisions`, the algorithm to compare two strings is simple:
  - Compare the first character of both strings.
  - If the first character from the first string is greater (or less) than the other string’s, then the first string is greater (or less) than the second. We’re done.
  - Otherwise, if both strings’ first characters are the same, compare the second characters the same way.
  - Repeat until the end of either string.
  - If both strings end at the same length and all characters are equal, then they are equal. Otherwise, the longer string is greater.
- The comparison algorithm given above is roughly equivalent to the one used in dictionaries or phone books, but it’s not exactly the same. It is the `unicode order`.
- When comparing values of different types, JavaScript converts the values to numbers.
- `==` VS `===`
  - `==` do type coersion on encountering different values while `===` do strict check
- For maths and other comparisons `<` `>` `<=` `>=` null/undefined are converted to numbers:
  - null becomes 0, while undefined becomes NaN.
- A Strange CASE of comparision:
  ```javascript
  alert(null > 0); // (1) false
  alert(null == 0); // (2) false
  alert(null >= 0); // (3) true
  ```
  - The results are simple to evaluate, > < >= <= convert them into number but in case of ==, undefined and null equal each other and don’t equal anything else.
  - Remember with undefined in upper example it will be false all the time as undefined convert to NaN and NaN is always false and with == undefined only equal null.

## 9

- Conditional branching can be done using `if-else if-else` ladder or `?` ternary operator.
- Curly braces are not required for a single-line body
- `if-else` is conditional execution and `?` is conditional assignment.
  - Syntax constructs that are not expressions cannot be used with the ternary operator ?, so no `break` and `continue`.
  - Reason not to use the question mark operator ? instead of if.
- We can chain multiple ternary operators condition under conditions.

## 10

- Logical operators are `&&` `||` `!` `??`.
- Remember about short circuiting.
- Precedence of AND `&&` is higher than OR `||`
- Although && and || act as replacement of if but, don’t replace if with || or &&.
- `!`, converts the operand to boolean type then returns the inverse value.
- `??` is null coalescing operator is just the OR operator but it only consider `undefined` and `null` as falsy value.
  - `||` returns the first truthy value.
  - `??` returns the first defined value.
- `??` has even lower precedence than `||`.
- Due to safety reasons, JavaScript forbids using ?? together with && and || operators, unless the precedence is explicitly specified with parentheses otherwise it will throw error.

## 11

- Loops are ways to repeat statements multiple times.
  - while
  - do while
  - for
    - begin executes once, and then it iterates: after each condition test, body and step are executed.
    - Any part of for can be skipped.
- Curly braces are not required for a single-line body
- To control loop we use `break` and `continue`.
- Syntax constructs that are not expressions cannot be used with the ternary operator ?, so no `break` and `continue`.
- break/continue support labels before the loop. A `label` is the only way for break/continue to escape a nested loop to go to an outer one.
  - A label is an identifier with a colon before a loop.
    ```javascript
    labelName: for (...) {
      ...
    }
    ```
  - `break <labelName>` or `continue <labelName>`.
  - Labels do not allow us to jump into an arbitrary place in the code.
  - `break <lablename>` looks upwards for the <lablename> and breaks out of that loop.

## 12

- The `switch` has one or more case blocks and an optional default and can replace multiple if checks.
- If there is no break then the execution continues with the next case without any checks, so we can say break are must but optional with default as it's the last check.
- Any `expression` can be a switch/case argument.
  ```javascript
  //grouped two cases
  case 3:
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;
  ```
- In switch the equality check is always strict.

## 13

- To create a function we can use a function declaration, function expression or arrow function.

  ```javascript
  // Function Declaration
  function name(parameter1, parameter2, ... parameterN) {
    ...body...
  }

  // Function Expression
  let varname = function(parameter1, parameter2, ... parameterN) {
    ...body...
  };
  ```

- `global` and `local` variables, It’s a good practice to minimize the use of global variables. Modern code has few or no globals.
- When a value is passed as a function parameter, it’s also called an argument.
  - A `parameter` is the variable listed inside the parentheses in the function declaration `it’s a declaration time term`.
  - An `argument` is the value that is passed to the function when it is called `it’s a call time term`.
  - JS is a very forgiving language we can pass less argument, more argument or exact number of argument it won't throw error.
    - If the arguments are less then asked then the rest will either take default(if given) or undefined.
    - If given more arguments then we can access the rest of them from `argument` keyword.
- If a function is called, but an argument is not provided, then the corresponding value becomes undefined, so to prevent that from happening we use default values.
- `return` control the flow of function, A function with an empty return or without it returns undefined.
- Functions should be short and do exactly one thing.
- Values passed to a function as parameters are copied to its local variables, `pass by value`.
- A function is a value, so we can deal with it as a value.
- Function Expression have a semicolon ; at the end.
- A Function Expression is created when the execution reaches it and is usable only from that moment.
- Function Declarations are processed before the code block is executed. They are visible everywhere in the block.
  - But in strict mode when a Function Declaration is within a code block, it’s visible everywhere inside that block. But not outside of it.
- Arrow functions are handy for one-liners. They come in two flavors:
  - `(...args) => expression` – the right side is an expression: the function evaluates it and returns the result.
  - `(...args) => { body }` – brackets allow us to write multiple statements inside the function, but we need an explicit return to return something.
  - Arrow functions are stored in a variable.
