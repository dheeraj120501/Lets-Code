# Introduction

Any function which calls itself is called recursive.

A recursive method solves a problem by calling a copy of itself to work on a smaller problem. This is called the recursion step.

The recursion step can result in many more such recursive calls.

It is important to ensure that the recursion terminates. Each time the function calls itself with a slightly simpler version of the original problem. The sequence of smaller problems must eventually converge on the base case.

- To get the idea of the base condition we usually do a dry run and create a reccursion tree.

Recursive code is generally shorter and easier to write than iterative code. Generally, loops are turned into recursive functions when they are compiled or interpreted.

Each recursive call makes a new copy of that method (actually only the variables) in memory (stack frame). Once a method ends (that is, returns some data), the copy of that returning method is removed from memory.

A recursive approach mirrors the problem that we are trying to solve. A recursive approach makes it simpler to solve a problem that may not have the most obvious of answers. But, recursion adds overhead for each recursive call (needs space on the stack frame).

Generally, iterative solutions are more efficient than recursive solutions (due to the overhead of function calls).

A recursive algorithm can be implemented without recursive function calls using a stack, but it’s usually more trouble than its worth. That means any problem that can be solved recursively can also be solved iteratively.

# Reccursion on Subsequences

## Print All | Print one | Count
