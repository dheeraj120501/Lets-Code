# Introduction

In computer science, a selection algorithm is an algorithm for finding the kth smallest number in a list or array; such a number is called the kth order statistic.

- This includes the cases of finding the minimum, maximum, and median elements.
- Selection is a subproblem of more complex problems like the nearest neighbor and shortest path problems.

There are O(n)-time (worst-case linear time) selection algorithms, and sublinear performance is possible for structured data; in the extreme, O(1) for an array of sorted data.

Many selection algorithms are derived by generalizing a sorting algorithm, and conversely some sorting algorithms can be derived as repeated application of selection.

The simplest case of a selection algorithm is finding the minimum (or maximum) element by iterating through the list, keeping track of the running minimum – the minimum so far – (or maximum) and can be seen as related to the selection sort.

The hardest case of a selection algorithm is finding the median. In fact, a specialized median-selection algorithm can be used to build a general selection algorithm, as in median of medians.

The best-known selection algorithm is Quickselect, which is related to Quicksort; like Quicksort, it has (asymptotically) optimal average performance, but poor worst-case performance, though it can be modified to give optimal worst-case performance as well.

## Famous Selection Algorithms

- QuickSelect
- PartialSelectionSort

# Partition Based Selection

For partition-based selection, the Quick select Algorithm is used.

It is a variant of quicksort algorithm.

In both, we choose a pivot element and using the partition step from the quicksort algorithm arranges all the elements smaller than the pivot on its left and the elements greater than it on its right. But while Quicksort recurses on both sides of the partition, Quickselect only recurses on one side, the side on which the desired kth element is present.

The median of an array is the best pivot for sorting of an array because it evenly divides the data into two parts., and thus guarantees optimal sorting, assuming the selection algorithm is optimal.

As in QuickSort if everytime we get the worst pivot we will end up sorting the complete array and the worst case time complexity will be O(N^2) which in practice is almost impossible as we use Randomized Version of it.

## Complexity

Time: O(N) in the average case, O(N2) in the worst case.

- Like quicksort, it is efficient in practice and has good average-case performance, but has poor worst-case performance.

Space: O(1)
