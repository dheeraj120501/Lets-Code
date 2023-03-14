# Introduction

# Hash Functions

## Collisions

## Load Factor and Resizing

Once your load factor is greater than .07, it’s time to resize your hash table.

Resizing is expensive, and you don’t want to resize too often. But averaged out, hash tables take O(1) even with resizing.

## Perfect Hash Function

# Collision Resolution Techniques

# Hash Tables

Put a hash function and an array together, and you get a data structure called a hash table.

They’re also known as hash maps, maps, dictionaries, and associative arrays.

# Bloom Filters

Some people might thing what is the use of this Data structure in the first place how about we just use a simple hashtable and store every possible instance.

- The motivation here is memory efficiency — you certainly could just store all the books themselves, but that would take far more memory than storing the bits needed for the bloom filter. For storing large amounts of data, this memory efficiency can matter quite a lot!

## Counting Bloom Filters

## Complexity Analysis

Search: O(1) (Best, Average), O(n) (Worst)
Insert: O(1) (Best, Average), O(n) (Worst)
Delete: O(1) (Best, Average), O(n) (Worst)

In the average case, hash tables are really fast.
In the worst case, a hash table takes O(n)—linear time for everything, which is really slow.

## Applications

Modeling relationships from one thing to another thing.
Hash tables are used for lookups on a large scale.
Checking for duplicates is very fast with a hash table.
Using hash tables as a cache.
