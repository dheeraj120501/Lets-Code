# Introduction

It is mostly used in optimization problem, a problem which demands either minimum or maximum result.

Greedy techniques can also be used as an approximation algorithm for complex problems.

Stratergies used for solving optimization problems are

- Greedy Method
- Branch and Bound
- Dynamic Programming

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage.

A greedy strategy does not produce an optimal solution, but a greedy heuristic can yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

- **In Laymen term, A greedy algorithm is an approach for solving a problem by selecting the best option available at the moment. It doesn't worry whether the current best result will bring the overall optimal result.**

It assumes that a local good selection makes for a global optimal solution.(Greedy Choice Property)

The algorithm never reverses the earlier decision even if the choice is wrong. It works in a top-down approach.

Making locally optimal choices does not always work. Hence, Greedy algorithms will not always give the best solutions and hence are not used for efficiency problems.

Greedy algorithms can be characterized as being 'short sighted', and also as 'non-recoverable'.

# Variations of Greedy Algorithm

Pure greedy algorithms
Orthogonal greedy algorithms
Relaxed greedy algorithms

# Using Greedy Properly

The algorithm can be used with any problem if the problem has the following properties:

1. **Greedy Choice Property**: If an optimal solution to the problem can be found by choosing the best choice at each step without reconsidering the previous steps once chosen, the problem can be solved using a greedy approach.

2. **Optimal Substructure**: If the optimal overall solution to the problem corresponds to the optimal solution to its subproblems, then the problem can be solved using a greedy approach.

## How to use Greedy Algorithm

To begin with, the solution set (containing answers) is empty.

At each step, an item is added to the solution set until a solution is reached.

If the solution set is feasible, the current item is kept else, the item is rejected and never considered again.

> In the end it all boils down to how we select the best feasible solution in each step, what criteria we select descides wether we get the optimal solution or not.

# Use Cases

- Sorting: Selection sort, Topological sort
- Priority Queues: Heap sort
- Optimal Merge Pattern Problem
- Huffman coding compression algorithm
- Fractional Knapsack Problem
- Disjoint sets-UNION by size and UNION by height (or rank)
- Single-Source Shortest Path Problem
- Coin change problem
- Job Scheduling Problem
- Prim’s and Kruskal’s Minimal Spanning Tree Algorithm
- Dijkstra's Minimal Spanning Tree Algorithm
- Dijkstra's Shortest Path Algorithm in Weighted Graphs
- Ford-Fulkerson Algorithm

## Examples

- The activity selection problem is characteristic of this class of problems, where the goal is to pick the maximum number of activities that do not clash with each other.

- In the Macintosh computer game Crystal Quest the objective is to collect crystals, in a fashion similar to the travelling salesman problem. The game has a demo mode, where the game uses a greedy algorithm to go to every crystal. The artificial intelligence does not account for obstacles, so the demo mode often ends quickly.

- The matching pursuit is an example of a greedy algorithm applied on signal approximation.

- A greedy algorithm finds the optimal solution to Malfatti's problem of finding three disjoint circles within a given triangle that maximize the total area of the circles; it is conjectured that the same greedy algorithm is optimal for any number of circles.

- A greedy algorithm is used to construct a Huffman tree during Huffman coding where it finds an optimal solution.

- In decision tree learning, greedy algorithms are commonly used, however they are not guaranteed to find the optimal solution.

- One popular such algorithm is the ID3 algorithm for decision tree construction.

- Dijkstra's algorithm and the related A\* search algorithm are verifiably optimal greedy algorithms for graph search and shortest path finding.

- A\* search is conditionally optimal, requiring an "admissible heuristic" that will not overestimate path costs.

- Kruskal's algorithm and Prim's algorithm are greedy algorithms for constructing minimum spanning trees of a given connected graph. They always find an optimal solution, which may not be unique in general.
