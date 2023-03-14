# Introduction

A graph is a non-linear data structure consisting of nodes that have data and are connected to other nodes through edges.

Nodes are also referred to as vertices. They store the data. The numbering of the nodes can be done in any order, no specific order needs to be followed.

Two nodes are connected by a horizontal line called Edge. Edge can be directed or undirected. Basically, pairs of vertices are called edges.

A graph does not necessarily mean to be an enclosed structure, it can be an open structure as well.

- A graph is said to have a cycle if it starts from a node and ends at the same node.
- There can be multiple cycles in a graph.

Number of edges that go inside or outside a node is called it's degree.

- For undirected graphs, the degree is the number of edges attached to a node.
- For directed graphs, we’ve Indegree and Outdegree. The indegree of a node is the number of incoming edges. The outdegree of a node is the number of outgoing edges.
- A terminal node is a node without any outgoing edges(i.e outdegree = 0).

Graph theory is the mathematical theory of the properties and applications of graphs (networks).

## Types of Graphs

**Undirected Graph**: An undirected graph is a graph in which edges have no orientation. The edge (u, v) is identical to the edge (v, u).

**Directed Graph (Digraph)**: A directed graph or digraph is a graph in which edges have orientations. For example, the edge (u, v) is the edge from node u to node v.

- In a directed graph, nodes have an indegree and an outdegree.
- Indegree can be seen as dependencies.

**Weighted Graphs**: Many graphs can have edges that contain a certain weight to represent an arbitrary value such as cost, distance, quantity, etc.

- Usually edge of a graph is denoted as a triplet (u, v, w) and specify whether the graph is directed or undirected.

## Special Graphs

**Tree**: A tree is an undirected connected graph with no cycles. Equivalently, it is a connected graph with N nodes and N-1 edges.

**Rooted Tree**: A rooted tree is a tree with a designated root node where every edge either points away from or towards the root node.

- When edges point away from the root the graph is called an **arborescence (out-tree)** and **anti-arborescence (in-tree)** otherwise.

**Directed Acyclic Graph**: DAGs are directed graphs with no cycles. These graphs play an important role in representing structures with dependencies.

- Several efficient algorithms exist to operates on DAGs.
- All out-trees are DAGs but not all DAGs are out-trees.

**Bipartite Graph**: A bipartite graph is one whose vertices can be split into two independent groups U, V such that every edge connects betweens U and V.

- A bipartite graph is a graph which can be coloured using 2 colours such that no adjacent nodes have the same colour.
- Any linear graph with no cycle is always a bipartite graph.
- With a cycle, any graph with an even cycle length can also be a bipartite graph. So, any graph with an odd cycle length can never be a bipartite graph.
- The graph is two colourable or there is no odd length cycle.
- If we are able to colour a graph with two colours such that no adjacent nodes have the same colour, it is called a bipartite graph.

**Complete Graph**: A complete graph is one where there is a unique edge between every pair of nodes. A complete graph with n vertices is denoted as the graph Kn.

## Representing Graphs

**Adjacency Matrix**: The idea is that the in the matrix cell m[i][j] represents the edge weight of going from node i to node j.

- It is often assumed that the edge of going from a node to itself has a cost of zero.
- Simplest graph representation.
- Space efficient for representing dense graphs.
- Edge weight lookup is O(1).
- Requires Θ(V²) space.
- Iterating over all edges takes Θ(V²) time.

**Adjacency List**: An adjacency list is a way to represent a graph as a map from nodes to lists of edges.

- Space efficient for representing sparse graphs.
- Iterating over all edges is efficient.
- Less space efficient for denser graphs.
- Edge weight lookup is O(E).
- Slightly more complex graph representation.

**Edge List**: An edge list is a way to represent a graph simply as an unordered list of edges. Assume the notation for any triplet (u,v,w) means: “the cost from node u to node v is w”.

- This representation is seldomly used because of its lack of structure. However, it is conceptually simple and practical in a handful of algorithms.
- Space efficient for representing sparse graphs.
- Iterating over all edges is efficient.
- Less space efficient for denser graphs.
- Edge weight lookup is O(E).

## Common Graph Theory Problems

**Connectivity**: Does there exist a path between node A and node B?

- Typical solution: Use union find data structure or any search algorithm (e.g DFS).

**Detecting Negative cycles**: Does my weighted digraph have any negative cycles? If so, where?

- Algorithms: Bellman-Ford and Floyd-Warshall.

**Minimum Spanning Tree (MST)**: A minimum spanning tree (MST) is a subset of the edges of a connected, edge-weighted graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

- MSTs on a graph are not always unique.
- MSTs are seen in many applications including: Designing a least cost network, circuit design, transportation networks, and etc.
- Algorithms: Kruskal’s, Prim’s & Borůvka's algorithm

**Shortest path problem**: Given a weighted graph, find the shortest path of edges from node A to node B.

- Algorithms: BFS (unweighted graph), Dijkstra’s, Bellman-Ford, Floyd-Warshall, A\*, and many more.

**Strongly Connected Components**: Strongly Connected Components (SCCs) can be thought of as self-contained cycles within a directed graph where every vertex in a given cycle can reach every other vertex in the same cycle.

- Algorithms: Tarjan’s and Kosaraju's algorithm

**Bridges**: A bridge / cut edge is any edge in a graph whose removal increases the number of connected components.

- Bridges are important in graph theory because they often hint at weak points, bottlenecks or vulnerabilities in a graph.

**Articulation points**: An articulation point / cut vertex is any node in a graph whose removal increases the number of connected components.

- Articulation points are important in graph theory because they often hint at weak points, bottlenecks or vulnerabilities in a graph.

**Network flow: (max flow)**: With an infinite input source how much “flow” can we push through the network?

- Algorithms: Ford-Fulkerson, Edmonds-Karp & Dinic’s algorithm

**Traveling Salesman Problem**: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?”

- The TSP problem is NP-Hard meaning it’s a very computationally challenging problem. This is unfortunate because the TSP has several very important applications.
- Algorithms: Held-Karp, branch and bound and many approximation algorithms

# Graph Traversal/Search Algorithms

Any traversal algorithm will always use a visited array.

## DFS Algorithm

The Depth First Search (DFS) is the most fundamental search algorithm used to explore nodes and edges of a graph.

- It runs with a time complexity of O(V+E) and is often used as a building block in other algorithms.
- A DFS plunges depth first into a graph without regard for which edge it takes next until it cannot go any further at which point it backtracks and continues.
- For DFS iteratively we need a stack or we can do it reccursively.

DFS is a traversal technique which involves the idea of recursion and backtracking. DFS goes in-depth, i.e., traverses all nodes by going ahead, and when there are no further nodes to traverse in the current path, then it backtracks on the same path and traverses other unvisited nodes.

We can have multiple DFS sequences.

```python
  # Global or class scope variables
  n = number of nodes in the graph
  g = adjacency list representing graph
  visited = [false, …, false] # size n
  function dfs(node):
      if visited[node]:
          return
      visited[node] = true

      neighbours = graph[node] # get all neighbours of a node
      for next in neighbours:
          dfs(next)
```

### Application of DFS

We can augment the DFS algorithm to:

- Compute a graph’s minimum spanning tree.
- Detect and find cycles in a graph.
- Check if a graph is bipartite.
- Find strongly connected components.
- Topologically sort the nodes of a graph.
- Find bridges and articulation points.
- Find augmenting paths in a flow network.
- Generate mazes.

## BFS Algorithm

The Breadth First Search (BFS) is a fundamental search algorithm used to explore nodes and edges of a graph.

- It runs with a time complexity of O(V+E) and is often used as a building block in other algorithms.
- The BFS algorithm is particularly useful for finding the shortest path on unweighted graphs.
- A BFS starts at some arbitrary node of a graph and explores the neighbour nodes first, before moving to the next level neighbours.
- For BFS iteratively we need a queue or we can do it reccursively

The BFS algorithm uses a queue data structure to track which node to visit next.

- Upon reaching a new node the algorithm adds it to the queue to visit it later.

We can have multiple BFS sequences.

```python
# Global/class scope variables
n = number of nodes in the graph
g = adjacency list representing unweighted graph
# s = start node, e = end node, and 0 ≤ e,s < n
function bfs(s, e):
    # Do a BFS starting at node s
    prev = solve(s)
    # Return reconstructed path from s -> e
    return reconstructPath(s, e, prev)
function solve(s):
    q = queue data structure with enqueue and dequeue
    q.enqueue(s)
    visited = [false, …, false] # size n
    visited[s] = true

    prev = [null, …, null] # size n
    while !q.isEmpty():
    node = q.dequeue()
    neighbours = g.get(node)
    for(next : neighbours):
    if !visited[next]:
    q.enqueue(next)
    visited[next] = true
    prev[next] = node
    return prev
function reconstructPath(s, e, prev):
    # Reconstruct path going backwards from e
    path = []
    for(at = e; at != null; at = prev[at]):
    path.add(at)

    path.reverse()
    # If s and e are connected return the path
    if path[0] == s:
    return path
    return []
```

## Applications of Traversal algorithms

### Detecting Cycles in A Graph

The cycle in a graph starts from a node and ends at the same node.

A graph can have connected components as well. In such cases, if any component forms a cycle then the graph is said to have a cycle.

One can use DFS/BFS and graph coloring to detect cycles.

#### Detecting Cycles in Undirected Graph

In a Undirected Cyclic Graph, during traversal, if we end up at a node, which we have visited previously in the path, that means we came around a circle and ended up at this node, which determines that it has a cycle.

#### Detecting Cycles in Directed Graph

In Directed Graphs we can't use the same logic of traversal as that in Undirected graphs.

- If a directed graph contains a cycle, the node has to be visited again on the same path and not through different paths. So slight modifications are required to make the previous algorithm work.

### Graph coloring method

Graph coloring is when you assign colors to the nodes in a graph.

- A legal coloring means no adjacent nodes have the same color.

If we are able to colour a graph with two colours such that no adjacent nodes have the same colour, it is called a bipartite graph.

Edge coloring is less common, but it's also a thing.

- A legal edge coloring means no nodes have two edges with the same color.

### Connected Components

Graphs can be connected or can be like a binary tree (as we know all trees are graphs with some restrictions).

Sometimes a graph is split into multiple components. It’s useful to be able to identify and count these components (islands).

A connected component or simply component of an undirected graph is a subgraph in which each pair of nodes is connected with each other via a path.

The number of connected components is equal to the number of independent sub graphs part of the original graph.

- One way to do so is by coloring each component with unique color meaning assigning an integer value to each group to be able to tell them apart.
- Algorithm: Start a DFS/BFS at every node (except if it’s already been visited) and mark all reachable nodes as being part of the same component.

```python
  # Global or class scope variables
  n = number of nodes in the graph
  g = adjacency list representing graph
  count = 0
  components = empty integer array # size n
  visited = [false, …, false] # size n
  function findComponents():
      for (i = 0; i < n; i++):
          if !visited[i]:
              count++
          dfs(i)
      return (count, components)
  function dfs(node):
      visited[node] = true
      components[node] = count
      for (next : g[node]):
          if !visited[next]:
              dfs(next)
```

# Topological Sorting

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.

The topological sort algorithm takes a directed acyclic graph (DAG) and returns an array of the nodes where each node appears before all the nodes it points to.

- The ordering of the nodes in the array is called a topological ordering.

- Cyclic graphs don't have a valid topological orderings.

Topological Sorting for a graph is not possible if the graph is not a DAG.

A graph can have more than one valid topological ordering.

## Application

The most common use for topological sort is ordering steps of a process where some the steps depend on each other.

The logic applies to any set of tasks with dependencies, like building components in a large software project, performing data analysis in Map-Reduce job, or bringing up hardware components at boot time. (For example, the mother board has to initialize the hard drive before the BIOS tries to load the bootloader from disk.)

In computer science, applications of this type arise in:

- Instruction scheduling
- Ordering of formula cell evaluation when recomputing formula values in spreadsheets
- Logic synthesis
- Determining the order of compilation tasks to perform in make files
- Data serialization
- Resolving symbol dependencies in linkers

## Topological Sorting with DFS based Approach

## Topological Sorting using Kahn's Algorithm

**Time Complexity**: O(V+E).

- The outer for loop will be executed V number of times and the inner for loop will be executed E number of times.

**Auxiliary Space**: O(V).

- The queue needs to store all the vertices of the graph. So the space required is O(V)

## All Topological Sorts of a DAG

We can go through all possible ordering via backtracking , the algorithm step are as follows :

- Initialize all vertices as unvisited.
- Now choose vertex which is unvisited and has zero indegree and decrease indegree of all those vertices by 1 (corresponding to removing edges) now add this vertex to result and call the recursive function again and backtrack.
- After returning from function reset values of visited, result and indegree for enumeration of other possibilities.

**Time Complexity**: O(V\*(V+E)), Here V is the number of vertices and E is the number of edges
**Auxiliary Space**: O(V), for creating an additional array and recursive stack space.

# Union-Find or Disjoint Sets

Given a set of N objects, connect two objects, or ask if two objects are connected (directly or in-directly).

- Connected components are subsets, each consists of connected objects.

An equivalence relation partitions the objects into equivalence classes or connected components.

- Reflexive: p is connected to p.
- Symmetric: If p is connected to q, then q is connected to p.
- Transitive: If p is connected to q, and q is connected to r, then p is connected to r.

**The Operations**:

- Find: In which component is object p ?
- Connected: Are objects p and q in the same component?
- Union: Connect two components containing objects p and q (if not already).

**Implementation Approaches**: It can be implemented by several different algorithms. 2 common approaches are Quick Find & Quick Union.

## Quick Find

Each object in the array has a value, or an id, and the id is it’s index initially. An element p is connected to element q if they have the same id.

### Union

When connecting two objects p and q, change the id of all objects that have the id of p to that of q, or vice-versa. So, we will have to loop on all array elements to check the id of each.

### Connected

Two objects are connected if and only if they have the same id.

### Complexity Analysis

It’s fast in checking whether there is a connection, slow in constructing the array of objects, and connecting objects.

Initialize & Union: O(N)
Connected: O(1)

## Quick Union

The array represent the parent of each object. Initially, the parent of an object is the object itself; every object is a root. We can imagine the data structure consists of trees, each tree has connected objects, and, trees mightn’t be connected together.

### Union

When connecting two objects p and q, connect the roots. So, change the parent of the root of p to the root of q, or vice-versa.

### Connected

Two objects are connected if their root is the same. So, we have to check the parents of each object up to the root.

### Complexity Analysis

It’s slow in checking whether there is a connection, slow in construct the array of objects, and connecting objects.

Initialize & Union & Connected → O(N).

# Minimum Spanning Tree (MST)

A Spanning tree is a tree that cover all the vertices with minimum possible edges.

Properties of a Spanning Tree:

- It is a subset of graph and that graph should be single component as if any two vertices are disconnected then one can't cover all the vertices and thus the ST can't be formed.
- Spanning trees can't be disconnected.
- It covers all the vertices with minimum possible edges and thus it's minimally connected i.e. removing any edge would disconnect the graph.
- ST is maximally acyclic i.e. adding 1 edge would make it cyclic.
- For V vertices the ST will have V-1 edges.
- We can never have any cycle in ST because covering V vertices with V-1 edges can't create loop.
- A connected Undirected graph have atleast 1 ST.
- A complete undirected graph have pow(V, V-2) no of possible ST.

A single graph can have many ST possible but the one with minimum cost (in weighted graphs) is called MST.

Minimum spanning tree has direct application in the design of networks, algorithms approximating the travelling salesman problem, multi-terminal minimum cut problem, minimum-cost weighted perfect matching, Cluster Analysis, Handwriting recognition, Image segmentation etc.

There are two famous algorithms for finding the Minimum Spanning Tree:

- Kruskal’s Algorithm
- Prim’s Algorithm

# Shortest Path Finding Algorithms

In graph theory, the shortest path problem is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized.

The shortest path problem can be defined for graphs whether undirected, directed, or mixed.

There are different variations of this problem:

- Single-pair shortest path problem
- Single-source shortest path problem
- Single-destination shortest path problem
- All-pairs shortest path problem

The most important algorithms for solving this problem are:

- Dijkstra's algorithm solves the single-source shortest path problem with non-negative edge weight.
- Bellman–Ford algorithm solves the single-source problem if edge weights may be negative.
- A\* search algorithm solves for single-pair shortest path using heuristics to try to speed up the search.
- Floyd–Warshall algorithm solves all pairs shortest paths.
- Johnson's algorithm solves all pairs shortest paths, and may be faster than Floyd–Warshall on sparse graphs.
- Viterbi algorithm solves the shortest stochastic path problem with an additional probabilistic weight on each node.

## Summary for shortest path algorithm

One source and One Destination

- Use A\* Search Algorithm (For Unweighted as well as Weighted Graphs).

One Source, All Destination

- Use BFS (For Unweighted Graphs)
- Use Dijkstra (For Weighted Graphs without negative weights)
- Use Bellman Ford (For Weighted Graphs with negative weights)

Between every pair of nodes-

- Floyd-Warshall
- Johnson’s Algorithm
