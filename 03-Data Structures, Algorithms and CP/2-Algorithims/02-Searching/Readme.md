# Introduction

Search algorithms work to retrieve information stored within some data structure, or calculated in the search space of a problem domain, with either discrete or continuous values.

Search algorithms are algorithms designed to search for or retrieve elements from a data structure, where they are stored. They are essential to access desired elements in a data structure and retrieve them when a need arises.

Search algorithms can be classified based on their mechanism into three types of algorithms:

- Linear
- Binary
- Hashing

## Application of Search Algorithms

Problems in combinatorial optimization, such as

- The vehicle routing problem, a form of shortest path problem
- The knapsack problem
- The nurse scheduling problem

Problems in constraint satisfaction, such as:

- The map coloring problem
- Filling in a sudoku or crossword puzzle

In game theory and especially combinatorial game theory, choosing the best move to make next (such as with the minmax algorithm)

Finding a combination or password from the whole set of possibilities

Factoring an integer (an important problem in cryptography)

Optimizing an industrial process, such as a chemical reaction, by changing the parameters of the process (like temperature, pressure, and pH)

Retrieving a record from a database

Finding the maximum or minimum value in a list or array

Checking to see if a given value is present in a set of values

# Linear Search

Linear search is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found.

Linear search is rarely practical because other search algorithms and schemes, such as the binary search algorithm and hash tables, allow significantly faster searching for all but short lists.

## Complexity Analysis

Time Complexity: O(n)
Space Complexity: O(1)

Linear search can be optimised a little using a sentinal value at the end of the list which results in fewer comparision. This optimised search is called **Sentinal Search**.

## Application

For searching operations in smaller arrays (<100 items).

Even though in theory other search algorithms may be faster than linear search, in practice even on medium-sized arrays (around 100 items or less) it might be infeasible to use anything else.

# Binary Search

Binary Search is a **searching algorithm** for finding an element's position **in a sorted array**.

Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first.

Binary search is faster than linear search except for small arrays.

Binary Search Algorithm can be implemented in two ways:

1. Iterative Method
2. Recursive Method (Divide and Conquer)

`low+((high-low)/2)` is better than `(low+high)/2` the former basically act as an overflow gaurd to help overcome the problem of overflow.

In terms of iterations, no search algorithm that works only by comparing elements can exhibit better average and worst-case performance than binary search.

There are specialized data structures designed for fast searching, such as hash tables, that can be searched more efficiently than binary search. However, binary search can be used to solve a wider range of problems, such as finding the next-smallest or next-largest element in the array relative to the target even if it is absent from the array.

Make sure you carefully find the search space. Binary search can be applied to anything where the search space is monotonic.

Variations of Binary search include

1. Uniform binary search
2. Exponential search
3. Interpolation search
4. Fractional cascading
5. Generalization to graphs
6. Noisy binary search
7. Quantum binary search

> Tip: If in a problem we have to do something with a sorted array and the time complexity required is something like logn then try binary search.

## Complexity Analysis

Time Complexities

- Best case complexity: O(1)
- Average case complexity: O(log n)
- Worst case complexity: O(log n)

Space Complexity

- The space complexity of the binary search is O(1).

## Application

In libraries of Java, .Net, C++ STL.
While debugging, the binary search is used to pinpoint the place where the error happens.

# Other Searching Algorithms

Ternary Search
Fibonacci Search
BFS & DFS

A vital aspect of search algorithms is Path Finding, which is used to find paths that can be taken to traverse from one point to another, by finding the most optimum route.

- A\* Path Finding Algorithm.

# CASE STUDY: How Google searches one document among Billions of documents quickly?

Whenever building a search engine we need 2 things low latency and high throughput.

Crawling -> Indexing -> Query

## Inverted Index

## Preprocessing

Converting all things to uppercase/lowercase, Stopwords, stemming, lemmatization, noise removal

# Conjunction (AND) / DisConjunction (OR) Query
