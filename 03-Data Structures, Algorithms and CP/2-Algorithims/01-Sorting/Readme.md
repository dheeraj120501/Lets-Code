# Introduction

Sorting is an algorithm that arranges the elements of a list in a certain order [either ascending or descending].

Sorting can significantly reduce the complexity of a problem, and is often used for database algorithms and searches.

A quick Google search reveals that there are over 40 different sorting algorithms used in the computing world today.

## Basic Terminologies

**In-Place Sort** algorithm is one in which we sort the list without any extraneous memory.

- It also doesn’t include the space used for stack in the recursive algorithms.

**Comparision Based Algorithm** means that we sort the list by comparing the elements in that list to one another.

- A comparator is defined to compare elements or items of a data sample. This comparator defines the ordering of elements.

**Counting-based sorting** mean there’s no comparison involved between elements in these types of sorting algorithms but rather work on calculated assumptions during execution.

An **unstable algorithm** is one in which the relative order amongst duplicate elements is not preserved.

When the occurrence of the elements to be sorted of an input array matters the time complexity of a sorting algorithm, then that algorithm is called **Adaptive sorting algorithm**.

Sort algorithms that use main memory exclusively during the sort are called **internal sorting algorithms**.

Sorting algorithms that use external memory, such as tape or disk, during the sort are called **external sorting algorithms**.

# Selection Sort

It is a **in-place**, **comparision based**, **unstable sorting algorithm**, this algorithm slowly builds an unsorted list into a sorted list by repeatedly searching for the **smallest value** and placing it in its correct location.

- With every outer iteration the smallest element get at it's correct position.

## Complexity Analysis

Time complexity = (n^2) (Best, Average, Worst)
Space complexity = O(1)

## Applications

Selection sort works well for small files. It is used for sorting the files with very large values and small keys. This is because selection is made based on keys and swaps are made only when required.

Selection sort is best suits for elements with bigger values and small keys.

Don't have much practical use in CS.

# Bubble Sort

It is a **in-place**, **comparision based**, **stable sorting algorithm** which repeatedly steps through an unsorted list compares adjacent elements and swaps them if they are in the wrong order the algorithm then repeats this process until the list is sorted.

- With every outer iteration the **largest element** bubbled to the top.

We have 2 variations of Bubble sort one a normal one and the other a little optimised one with flag with modified version best case of bubble sort improved to O(n).

## Complexity Analysis

Time complexity = (n) (Best), (n^2) (Average, Worst)
Space complexity = O(1)

## Applications

The only significant advantage that bubble sort has over other implementations is that it can detect whether the input list is already sorted or not

Don't have much practical use in CS.

# Cocktail Shaker Sort

It is a **in-place**, **comparision based**, **stable sorting algorithm** which repeatedly steps through an unsorted list compares adjacent elements and swaps them if they are in the wrong order.

- With every outer iteration the **largest element** bubbled to the top and the **smallest one** sinks at the bottom.

It's just like optimised bubble sort but just a little optimised, here we traverse back and forth the list like we are shaking a cocktail as opposed to just forward like in bubble sort.

## Complexity Analysis

Time complexity = (n) (Best), (n^2) (Average, Worst)
Space complexity = O(1)

## Applications

Don't have much practical use in CS.

# Odd-Even Sort

Odd-Even sort is a variation on bubble sort which sorts the list through two phases an odd phase and an even phase during the odd phase we perform a bubble sort on odd indexed elements and during the even phase we perform a bubble sort on even indexed elements.

It's just like optimised bubble sort but just a little optimised, here we traverse back and forth the list like we are shaking a cocktail.

## Complexity Analysis

Time complexity = (n) (Best), (n^2) (Average, Worst)
Space complexity = O(1)

## Applications

Odd-Even sort is mainly used on parallel processors with local interconnections for running local tasks.

# Merge sort

Merge sort is a **stable** sorting algo which is not in place as the merging step requires extra space to store the elements..

Merge sort algorithm is called 2-way merging.

- If we merge K files at a time then we call it K-way merging.

## Complexity Analysis

Time Complexity = O(N log(N)) in all 3 cases (worst, average, and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.

Space Complexity = O(n), In merge sort all elements are copied into an auxiliary array. So N auxiliary space is required for merge sort.

## Applications

Merge Sort is useful for sorting linked lists in O(N log N) time using something like quick sort for LL adds a lot of overhead.

- In a linked list to access i’th index, we have to travel each and every node from the head to i’th node as we don’t have a contiguous block of memory. Therefore, the overhead increases for quicksort. Merge sort accesses data sequentially and the need of random access is low.

Inversion Count Problem

As merge sort can handle large datasets, it is often used for external sorting, where the data being sorted does not fit in memory.

- Although effecient for large datasets its not the best choice for small datasets.

The merge sort algorithm can be easily parallelized, which means it can take advantage of multiple processors or cores to sort the data more quickly.

Merge sort requires relatively few additional resources (such as memory) to perform the sort. This makes it a good choice for systems with limited resources.

# Quick Sort

Quicksort is one of the fastest sorting algorithms out there, and it’s a very good example of D&C.

## Pseudocode

1. Pick a pivot.
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
3. Call quicksort recursively on the two sub-arrays.

## Partitioning

Quicksort is unique because its speed depends on the pivot you choose i.e. it's performance heavily depends on the pivot you choose.

Quicksort doesn’t check to see whether the input array is already sorted.

## Complexity Analysis

Time Complexity = O(nlogn) (Best and Average), O(n^2) (Worst)
Space Complexity = O(n) (Worst)

## Quick Sort VS Merge Sort

When we analyse any two algorithms we usually neglect lower terms and constants, because if two algorithms have different Big O times, the constant doesn’t matter.

- This is only good but if both the algorithms have different curve equation.

- The constant in Big O notation can matter sometimes. That’s why quicksort is faster than merge sort.

- Quicksort has a smaller constant than merge sort. So if they’re both O(n log n) time, quicksort is faster.

Quicksort is faster in practice because it hits the average case way more often than the worst case (Ostritch Algo.).

## Applications

# Cycle Sort

## Complexity Analysis

Time Complexity =
Space Complexity =

## Applications

# Bitonic Sort

## Bitonic Sequences

## Complexity Analysis

Time Complexity =
Space Complexity =

## Applications

# Bucket Sort

Bucket Sort assumes that a random process that distributes elements uniformly over the interval generates the input.

## Hashing Algorithm

Stability of bucket sort depends upon the stability of the underlying sorting algorithm used to sort items of each bucket.

## Complexity Analysis

Time Complexity = O(n+k) (Best and Average), O(n^2) (Worst)
Space Complexity = O(n+k) (Worst)

## Applications

This is mainly used when the data is uniformaly distributed.

# Radix Sort

Radix Sort assumes that the input consists of an integer in a small range.

## Complexity Analysis

Time Complexity =
Space Complexity =

## Applications

# Counting Sort

It is a linear time sorting algorithm which works faster by not making a comparison.

It assumes that the number to be sorted is in range 1 to k where k is small.

Basic idea is to determine the "rank" of each number in the final sorted array.

## Complexity Analysis

Time Complexity =
Space Complexity =

## Applications

# Tree Sort

## Representing Tree as an Array

## Complexity Analysis

Time Complexity =
Space Complexity =

## Applications

# Heap Sort

## Representing Heap as an Array

## Complexity Analysis

Time Complexity =
Space Complexity =

## Applications

# Insertion Sort

Insertion sort is used when the data is nearly sorted (due to its adaptiveness) or when the input size is small (due to its low overhead).

Due to its stability, insertion sort is used as the recursive base case (when the problem size is small) for higher overhead divide-and-conquer sorting algorithms, such as merge sort or quick sort.

Insertion sort is almost linear for partially sorted input.

## Complexity Analysis

Time Complexity =
Space Complexity =

## Applications

# Shell Sort

## Complexity Analysis

Time Complexity =
Space Complexity =

## Applications

# External Sort - External merge sort

External sorting is a term for a class of sorting algorithms that can handle massive amounts of data.

It is required when the data being sorted does not fit into the main memory of a computing device (usually RAM) and instead, must reside in the slower external memory (usually a hard drive).

External sorting algorithms generally fall into two types, distribution sorting, which resembles quicksort, and external merge sort, which resembles merge sort.

External merge sort typically uses a hybrid sort-merge strategy which includes 2 Phases.

- In the sorting phase, chunks of data small enough to fit in the main memory are read, sorted, and written out to a temporary file.
- In the merge phase, the sorted sub-files are combined into a single larger file.

## K-way mrerging

In computer science, k-way merge algorithms or multiway merges are a specific type of sequence merge algorithms that specialize in taking in k sorted lists and merging them into a single sorted list.

k-way merges are used in external sorting procedures.

**Iterative 2-way merge**: Here the process starts by iteratively merging two of the k arrays using a 2-way merge until only a single array is left.

- If the arrays are merged in arbitrary order, then the resulting running time is only O(kn). This is suboptimal.

- The running time can be improved by iteratively merging the first with the second, the third with the fourth, and so on. As the number of arrays is halved in each iteration, and in each iteration every element is moved exactly once. The running time per iteration is therefore in Θ(n) as n is the number of elements making total running time as Θ(n log k).

- We can further improve upon this algorithm, by iteratively merging the two shortest arrays. It is clear that this minimizes the running time and can therefore not be worse than the strategy described in the previous paragraph. The running time is therefore in O(n log k). Fortunately, in border cases the running time can be better.

**Direct k-way merge**: In this case, we would simultaneously merge k-runs together.

- A straightforward implementation would scan all k arrays to determine the minimum. This straightforward implementation results in a running time of Θ(kn). Although it would work, it is not efficient.

- We can improve upon this by computing the smallest element faster. By using either **heaps**, **tournament trees**, or **splay trees**, the smallest element can be determined in O(log k) time. The resulting running times are therefore in O(n log k).

## Merging K Sorted Arrays

There are many ways to do Merging K Sorted Arrays.

Given K sorted arrays of size N each.

- One naive way is to create an output array of size (N \* K) and then copy all the elements into the output array followed by sorting.

  - Time Complexity: O(N \* K \* log (N\*K)), Since the resulting array is of size N\*K.
  - Space Complexity: O(N \* K), The output array is of size N \* K.

- Start by merging arrays into groups of two. After the first merge, there will be K/2 arrays remaining. Again merge arrays in groups, now K/4 arrays will be remaining. This is similar to merge sort. Divide K arrays into two halves containing an equal number of arrays until there are two arrays in a group. This is followed by merging the arrays in a bottom-up manner. This is Iterative 2-way merge of K-way merging.

  - Time Complexity: O(N \* K \* log K). There are log K levels as in each level the K arrays are divided in half and at each level, the K arrays are traversed.
  - Auxiliary Space: O(N \* K \* log K). In each level O(N \* K) space is required.

- One other way is to use Min-Heap. This Min-Heap based solution has the same time complexity which is O(N\*K\*log K). But for a different and particular sized array, this solution works much better. The process must start with creating a Min-Heap and inserting the first element of all the k arrays. Remove the root element of Minheap and put it in the output array and insert the next element from the array of removed element. To get the result the step must continue until there is no element left in the Min-Heap. This is Direct k-way merge of K-way merging.

  - Time Complexity: O(N \* K \* log K), Insertion and deletion in a Min Heap requires log K time.
  - Auxiliary Space: O(K), If Output is not stored then the only space required is the Min-Heap of K elements.

There might also be a case when the given k sorted arrays are of possibly different sizes.

- A simple solution is to create an output array and one by one copy all k arrays to it. Finally, sort the output array. This approach takes O(N Log N) time where N is the count of all elements.

- An efficient solution is to use a heap data structure. The time complexity of the heap-based solution is O(N Log k).

## Complexity Analysis

Time Complexity =
Space Complexity =

## Applications

# Inbuilt sorting algorithms of different programming languages and the algorithm they use internally

**C++**: The sorting algorithm used by the C++ standard library, in both GCC and MSVC, is called **introsort**.

- It is a hybrid of quick sort, heap sort and insertion sort.
- It uses quicksort until it hits a certain recursion depth, at which point it switches to heapsort in order to maintain the required O(nlogn) worst-case behavior. (Otherwise, quicksort can devolve to O(n^2) in some pathological cases.)
- On sufficiently random data, it is effectively pure quicksort, since it should seldom (if ever) get to a deep enough recursion level to switch over.

**Python**: Pythons build in sort is called **TimSort**.

- Its a merge sort and insertion sort hybrid.

**Java**: The collections' sort algorithm uses **merge sort** while the Array.sort uses **timsort**.

# When to use which sorting technique

If the occurrence of the same element important

- Use: Insertion, Bubble, Merge, Quick
- Don't Use: Heap, Quick

If the data size small

- Use: Insertion, Bubble
- Don't Use: Heap, Merge, Quick

If memory for extra space an issue

- Use: Insertion, Bubble, Heap
- Don't Use: Merge, Quick

If the input data nearly sorted

- Use: Insertion, Bubble
- Don't Use: Heap, Merge, Quick

If speed important

- Use: Heap, Merge, Quick
- Don't Use: Insertion, Bubble

## Conclusion

For small dataset any algorithm is good.
For medium dataset of 60-1k items comparision sorts are great.
For large dataset radix sort is the boss.

There are some algorithms that runs faster and takes linear time such as Counting Sort, Radix Sort, and Bucket Sort but they require the special assumption about the input sequence to sort.

# Misc

There are a lot of other complex and funny sorting algorithms as well.

1. **Bogocounting sort**: Create an array of all possible elements. Select a random index in the array and a random index in the list until the element is found, then put it in the sorted list.

2. **Natural selection sort**: Score the list using a fitness function (such as number of items out of order) then copy it but introduce some random swapping of items. Check a random list. If that list has at least the best score so far, reproduce the list but mutate it. If the list does not have the best score so far, delete the list. The list is considered sorted when it has equal fitness to a sorted list.

3. **Adaptation sort**: Inspired by natural selection sort but trimmed down to improve speed and memory usage. Count the number of inversions in the list. Randomly swap two items and check their immediate neighbors to see if it reduces inversions. If it doesn't, then undo the swap. Repeat until there are no inversions.

4. **Stooge sort**: Stooge Sort is a recursive sorting algorithm. It is not much efficient but interesting sorting algorithm. It generally divides the array into two overlapping parts (2/3 each). After that it performs sorting in first 2/3 part and then it performs sorting in last 2/3 part. And then, sorting is done on first 2/3 part to ensure that the array is sorted.

- The key idea is that sorting the overlapping part twice exchanges the elements between the other two sections accordingly.

- The running time complexity of stooge sort can be written as O(n^(log3/log1.5)) = O(n^2.709) hence it is slower than even bubble sort(n^2).

5. **Bogo sort**: BogoSort also known as permutation sort, stupid sort, slow sort, shotgun sort or monkey sort is a particularly ineffective algorithm one person can ever imagine.

- It is based on generate and test paradigm. The algorithm successively generates permutations of its input until it finds one that is sorted.

6. **Sleep Sort**: In this algorithm we create different threads for each of the elements in the input array and then each thread sleeps for an amount of time which is proportional to the value of corresponding array element.

- This way the thread having the least amount of sleeping time wakes up first and the number gets printed and then the second least element and so on. The largest element wakes up after a long time and then the element gets printed at the last. Thus the output is a sorted one.

- This algorithm won’t work for negative numbers as a thread cannot sleep for a negative amount of time.

- Sleep Sort is related to Operating System more than any other sorting algorithm. This sorting algorithm is a perfect demonstration of multi-threading and scheduling done by OS.
