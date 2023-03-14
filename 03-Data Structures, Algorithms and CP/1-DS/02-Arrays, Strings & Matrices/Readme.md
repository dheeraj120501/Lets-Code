# Subarray vs Substring vs Subsequence vs Subset

A subarray is a contiguous sequence of elements within an array.

- For instance, the subarrays of the array {1, 2, 1} would be {1}, {2}, {1, 2}, {2, 1}, {1, 2, 1}, {}.
- A subarray should be a contiguous subsequence of the parent array.
- The full array itself is a subarray of itself.
- An empty array is a subarray of any array.
- Order of elements in the subarray should be the same as in the array.

A substring is exactly the same thing as a subarray but in the context of strings.

- For instance, the substrings of the string "ara" would be "a", "r", "ar", "ra", "ara", "".
- A substring is just a subarray that is made up of only characters.

Both in mathematics and computer science, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

- Subsequence is a generalized subarray, where the rule of contiguity does not apply.
- Unlike subarrays, subsequences do not need to be contiguous.
- Subsequences still need to preserve element order just like subarrays.

A set is subset of another set if all its elements are contained by that set.

- This means, neither contiguity nor ordering of elements matter.
- For instance, the subsets of the set {1, 2, 3} would be {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}, {}.
- Subsets do not need to be contiguous.
- Subsets do not need to preserve element order.
- Unlike arrays, strings, and sequences, sets do not allow duplicate elements.

## Comparison Table

|                  | Subarray | Substring | Subsequence | Subset |
| ---------------- | -------- | --------- | ----------- | ------ |
| Contiguous       | Yes      | Yes       | No          | No     |
| Elements Ordered | Yes      | Yes       | Yes         | No     |

# Problems

1. We are given two sorted arrays. We need to merge these two sorted arrays such that the initial numbers (after complete sorting) are in the first array and the remaining numbers are in the second array but with O(1) extra space.

- This task is simple and O(m+n) if we are allowed to use extra space.

  - But it becomes really complicated when extra space is not allowed and doesn’t look possible in less than O(m\*n) worst-case time. Though further optimizations are possible.

- M\-1: 2 Pointers and Insertion sort

  - The ides is to begin from the last element of ar2[] and search for it in ar1[].
  - If there is a greater element in ar1[], then we move the last element of ar1[] to ar2[].
  - To keep ar1[] and ar2[] sorted, we need to place the last element of ar2[] at the correct place in ar1[]. We can use the Insertion Sort for this.
  - Time Complexity: O(M \* N)
  - Auxiliary Space: O(1)

- M\-2: Optimization

  - The solution can be further optimized by observing that while traversing the two sorted arrays parallelly, if we encounter the jth second array element being smaller than ith first array element, then the jth element is to be included and replace some kth element in the first array.
  - Then Sort both arr1 and arr2 individually.
  - Time Complexity: O((N+M) \* log(N+M))
  - Auxiliary Space: O(1)
