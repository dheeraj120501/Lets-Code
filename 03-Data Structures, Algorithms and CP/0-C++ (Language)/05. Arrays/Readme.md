Arrays are useful for storing collection of similar data type together. Arrays are useful when we want to store set of values in our program, then we use array of data items.

Decleration
int a[5]; // We are able to store 5 integers in continuous memory block

Decralation and Defination
int b[5] = {1,2,3,5,8}; // Declaration with size and initialization
int c[] = {1,5,8,6,7,136,65}; // Declaration without size with initialization, size will be the total elements during initialization
int d[5] = {1,2} // Declaration with size but partial initialization, remaining will be zero
int e[5] = {0}; // Declaration with partial initialization. All the values in the array becomes zero.

There are 2 methods of searching : 1. Linear Search O(n) 2. Binary Search (Requires sorted array) O(logn)
