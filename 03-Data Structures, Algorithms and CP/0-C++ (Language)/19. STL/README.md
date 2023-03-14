# Data Structures

To store the collection of values we need data structures. Arrangement of data for efficient utilization is what the study of Data Structures is all about. Efficiency is measured on 2 parameters time and space. CPP provides arrays, but problem is that it is of fixed size which can't be modified as per the need.

Another Data Structure is Linked List, Size of LL can grow and reduce as per the numbers being inserted or deleted. Easy to create new nodes in a LL. There are doubly as well as circular linked lists too.

Some of the other Data Structures are: Stack, Queue, Dequeue, Priority Queue, Map, Set, Graphs etc. So, as a programmer do we have to define all these data structures before using them in our program ? No, we don't have to do that. C++ provides built-in library of classes for all these data structures and that is collection of classes called as STL.

There are some collection of header files having many classes in them and that collection is called as STL. There is class available for LL, arrays, stack etc.

# Standard Template Library (STL)

STL has **algorithms**, **containers** and **iterators**. There are built-in algorithms of functions that are meant to manage the containers. Containers contain collection of data. There are iterators to iterate through the collection of values. To access the containers we have iterators available. Algorithms contain, search(), sort(), binary-search(),concat(),copy(),union(), reverse(),merge(),heap() are some of the functions that are available to be called on containers

Containers: These are template classes, can work for any kind of data.

1. **vector**: Array that can grow and reduce as per the input. Has functions like **push_back()**, **pop_back()**,**insert()**,**remove()**,**size()** and **empty()**.

2. **list**: **Doubly linked list**. Has functions same as vector but additional ones like **push_front()**,**pop_front()**,front(), back() etc.

3. **forward_list**: **Single linked list**, introduced in C11. As double linked list needs space for pointer to next and previous node.

4. **dequeue**: Dequeue is like vector only but it means double ended queue and we can delete and insert from both the ends. List, forward_list and dequeue has same set of functions. Only in vector we can't insert from front.

5. **priority_queue**: **Heap** data structure. **Max-heap** to be specific. push(), pop(),empty(),size() same operations as stack present for priority queue as well. Priority queue basically means the largest element from the queue will be deleted.

6. **stack**: Follows LIFO has same set of operations as priority queue we see above.

7. **set**: Collection of elements that contains unique elements and does not maintains the order.

8. **Multiset**: Same as set but allows duplicates.

9. **Map**: To store **key-value** pairs. Like Dictionary in Python. Contains unique keys, can't have 2 keys with same content. Uses hash tables. Similarly we have **multimap** as you might have guessed this allows keys to be duplicated just like multiset. Duplicate keys are allowed but same key-value pair is still not allowed.

# Iterators

An iterator is an object designed to traverse through a container (e.g. the values in an array, or the characters in a string), providing access to each element along the way.

Iterating through a data structure is quite a common thing to do in programming which can be done in different ways:

- Using loops and an index (for-loops and while loops): Looping using indexes is more typing than needed if we only use the index to access elements. It also only works if the container (e.g. the array) provides direct access to elements (which arrays do, but some other types of containers, such as lists, do not).

```cpp
std::size_t index{ 0 };
while (index < length)
{
    std::cout << data[index] << ' ';
    ++index;
}
std::cout << '\n';

for (std::size_t index = 0; index < length; ++index)
{
    std::cout << data[index] << ' ';
}
std::cout << '\n';
```

- Using pointers and pointer arithmetic: Looping with pointers and pointer arithmetic is verbose, and can be confusing to readers who don’t know the rules of pointer arithmetic. Pointer arithmetic also only works if elements are consecutive in memory (which is true for arrays, but not true for other types of containers, such as lists, trees, and maps).

```cpp
for (auto ptr{ &data[0] }; ptr != (&data[0] + length); ++ptr)
{
    std::cout << *ptr << ' ';
}
std::cout << '\n';
```

- Using range-based for-loops: They use iterators.

```cpp
for (int i : data)
{
    std::cout << i << ' ';
}
std::cout << '\n';
```

A container may provide different kinds of iterators.

- For example, an array container might offer a forwards iterator that walks through the array in forward order, and a reverse iterator that walks through the array in reverse order.

Once the appropriate type of iterator is created, the programmer can then use the interface provided by the iterator to traverse and access elements without having to worry about what kind of traversal is being done or how the data is being stored in the container.

As C++ iterators typically use the same interface for traversal (operator++ to move to the next element) and access (operator\* to access the current element), we can iterate through a wide variety of different container types using a consistent method.

- The iterator takes care of the details of iterating through the container. All we need are four things: the begin point, the end point, operator++ to move the iterator to the next element (or the end), and operator\* to get the value of the current element.

- Behind the scenes, the range-based for-loop calls `begin()` and `end()` of the type to iterate over.

Much like pointers and references, iterators can be left **dangling** if the elements being iterated over change address or are destroyed. When this happens, we say the iterator has been invalidated.

- Accessing an invalidated iterator produces undefined behavior.

Ref:**stl.cpp**

# Algorithms

## Binary Search

Lower Bound and Upper Bound
