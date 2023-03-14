# String Searching Algorithms

In computer science, string-searching algorithms, sometimes called string-matching algorithms, are an important class of string algorithms that try to find a place where one or several strings (also called patterns) are found within a larger string or text.

The method of feasible string-search algorithm may be affected by the string encoding.

The most basic case of string searching involves one (often very long) string, sometimes called the haystack, and one (often very short) string, sometimes called the needle.

- The goal is to find one or more occurrences of the needle within the haystack.

Another more complex type of search is regular expression searching, where the user constructs a pattern of characters or other symbols, and any match to the pattern should fulfill the search.

Given two strings, maximal exact matchings (MEMs) are common substrings that cannot be extended left or right without causing a mismatch.

There are different types of method is used to finding the string:

- The Naive String Matching Algorithm
- The Rabin-Karp-Algorithm
- Finite Automata
- The Knuth-Morris-Pratt Algorithm
- The Boyer-Moore Algorithm

## KMP algorithm

## Summary

| Algorithm          | Preprocessing Time | Matching Time           |
| ------------------ | ------------------ | ----------------------- |
| Naive              | O                  | O (n - m + 1)m          |
| Rabin-Karp         | O(m)               | O (n - m + 1)m          |
| Finite Automata    | O(m\|∑\|)          | O (n)                   |
| Knuth-Morris-Pratt | O(m)               | O (n)                   |
| Boyer-Moore        | O(\|∑\|)           | O ((n - m + 1) + \|∑\|) |
