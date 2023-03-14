# Introduction

Backtracking is an improvement of the brute force approach.

It systematically searches for a solution to a problem among all available options. In backtracking, we start with one possible option out of many available options and try to solve the problem.

If we are able to solve the problem with the selected move then we will print the solution else we will backtrack and select some other option and try to solve it.

If none if the options work out we will claim that there is no solution for the problem.

Backtracking can be thought of as a selective tree/graph traversal method.

Backtracking allows us to deal with situations in which a raw brute-force approach would explode into an impossible number of options to consider.

# Parameterised and Functional Recursion

# Multiple Recursion Calls

## Time Complexity with multiple reccursion calls

With Single reccursion call the time complexity is of O(n) where n is the depth of reccursion tree.

With Multiple reccursion calls the time complexity is exponential in nature.

Time Complexity: O(pow(k,n)) where n is the depth of reccursion tree and k is the number of reccursion calls in function.
