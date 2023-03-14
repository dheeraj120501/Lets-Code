> `Those who cannot remember the past are condemned to repeat it. — Dynamic Programming.`

# **Credits and Resources**

[Video Lesson on DP](https://www.youtube.com/watch?v=oBt53YbR9Kk, "Video Lesson on DP")

[Beginner's Guide to DP](https://leetcode.com/problems/min-cost-climbing-stairs/discuss/773865/A-Beginner's-Guide-on-DP-validation-and-How-to-come-up-with-a-Recursive-solution-Python-3, "Beginner's Guide to DP")

# **Basic Theory**

The core idea of Dynamic Programming is to avoid repeated work by remembering partial results and this concept finds it application in a lot of real life situations.

The intuition behind dynamic programming is that we trade space for time, i.e. to say that instead of calculating all the states taking a lot of time but no space, we take up space to store the results of all the sub-problems to save time later.

In programming, Dynamic Programming is a powerful technique that allows one to solve different types of problems in polynomial time for which a naive approach would take exponential time.

Some famous Dynamic Programming algorithms are:

- Unix diff for comparing two files
- Bellman-Ford for shortest path routing in networks
- TeX the ancestor of LaTeX
- WASP - Winning and Score Predictor

Dynamic Programming is not an algorithm or data-structure. It is a technique and it is applied to a certain class of problems.

## **Properties of DP**

**Optimal substructure**: Can the optimal solution be constructed from the optimal solutions of its subproblems? (Are the subproblems independent from each other?

**Overlapping subproblems**: Does finding the solution require us to calculate the same subproblem multiple times?

Once a problem have both properties fulfilled, we know that we can tackle this problem using DP with confidence!

- We need to break up a problem into a series of overlapping sub-problems, and build up solutions to larger and larger sub-problems.

- If you are given a problem, which can be broken down into smaller sub-problems, and these smaller sub-problems can still be broken into smaller ones, and if you manage to find out that there are some over-lappping sub-problems, then you've encountered a DP problem.

Majority of the Dynamic Programming problems can be categorized into two types:

1. Optimization problems, which expect you to select a feasible solution, so that the value of the required function is minimized or maximized.
2. Combinatorial problems, which expect you to figure out the number of ways to do something, or the probability of some event happening.

# **Memoization**

If you implement your function in a way that the recursive calls are done in advance, and stored for easy access, it will make your program faster.

This is what we call Memoization, it is memorizing the results of some specific states, which can then be later accessed to solve other sub-problems.

## **Using Memoization**

Uses a recursion

1. Make it work
   1. Visualize the problem as a tree
   2. Implement the tree using recursion
   3. Test it
2. Make it efficient
   1. Add a memo object
   2. Add a base base to return memo values
   3. Store return values into the memo

# **Tabulation**

## **Using Tabulation**

Uses iteration

1. Visualize the problem as a table
2. Size the table based on inputs
3. Initialize the table with default values
4. Seed the trivial answer in the table
5. Iterate through the table
6. Fill further positions based on the current position

# **Dynamic programming vs Memoization vs Tabulation**

Dynamic programming is a technique for solving problems of recursive nature, iteratively and is applicable when the computations of the subproblems overlap.

- Dynamic programming is typically implemented using tabulation, but can also be implemented using memoization. So as you can see, neither one is a "subset" of the other.

A tabulation algorithm focuses on filling the entries of the cache, until the target value has been reached.

- When you solve a dynamic programming problem using tabulation you solve the problem **bottom up**, i.e., by solving all related sub-problems first, typically by filling up an n-dimensional table. Based on the results in the table, the solution to the "top" / original problem is then computed.

- A tabulation implementation is always iterative.

- If the original problem requires all subproblems to be solved, tabulation usually outperformes memoization by a constant factor. This is because tabulation has no overhead for recursion and can use a preallocated array rather than, say, a hash map.

  - There are some problems for which the regular pattern of table accesses in the dynamic-programming algorithm can be exploited to reduce the time or space requirements even further.

Memoization is a term describing an optimization technique where you cache previously computed results, and return the cached result when the same computation is needed again.

- If you use memoization to solve the problem you do it by maintaining a map of already solved sub problems. You do it "top down" in the sense that you solve the "top" problem first (which typically recurses down to solve the sub-problems).

- If only some of the subproblems need to be solved for the original problem to be solved, then memoization is preferrable since the subproblems are solved lazily, i.e. precisely the computations that are needed are carried out.

# **State space reduction**

In problems for which dynamic programming solutions are considered, there is a concept of a state.

A state is, in general, a point in a d-dimensional space, where d is called the number of dimensions in the solution.

# **Dynamic Programming and Bit Masking**

# **Complexity Analysis of sample problems**

## Grid Traveler

n: number of rows
m: number of columns

- Brute force
  - Time: `2^(n + m)`
  - Space: `n + m`
- Memoized
  - Time: `n * m`
  - Space: `n + m`
- Tabulation
  - Time: `n * m`
  - Space: `n * m`

## Can Sum

m: target sum (length)
n: number of array elements

- Brute force
  - Time: `n^m`
  - Space: `m`
- Memoized
  - Time: `n * m`
  - Space: `m`
- Tabulation
  - Time: `n * m`
  - Space: `m`

## How Sum

m: target sum
n: number of array elements

- Brute force
  - Time: `n^m * m`
  - Space: `m`
- Memoized
  - Time: `n * m^2`
  - Space: `m^2`
- Tabulation
  - Time: `n * m^2`
  - Space: `m^2`

## Best Sum

m: target sum
n: number of array elements

- Brute force
  - Time: `n^m * m`
  - Space: `m^2`
- Memoized
  - Time: `n * m^2`
  - Space: `m^2`

## Can Construct

m: target string length
n: number of array elements

- Brute force
  - Time: `n^m * m`
  - Space: `m^2`
- Memoized
  - Time: `n * m^2`
  - Space: `m^2`
- Tabulation
  - Time: `n * m^2`
  - Space: `m^2`

## Count Construct

m: target string length
n: number of array elements

- Brute force
  - Time: `n^m * m`
  - Space: `m^2`
- Memoized
  - Time: `n * m^2`
  - Space: `m^2`

## All Construct

m: target string length
n: number of array elements

- Brute force
  - Time: `n^m`
  - Space: `m`
- Memoized
  - Time: `n^m`
  - Space: `m`
- Table
  - Time: `n^m`
  - Space: `n^m`
