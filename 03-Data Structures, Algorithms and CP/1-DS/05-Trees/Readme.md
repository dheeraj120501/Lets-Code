# Introduction

A tree is a data structure similar to a linked list but instead of each node pointing simply to the next node in a linear fashion, each node points to a number of nodes.

Tree is a **non-linear** data structure.

Order of the elements is not important if we need ordering information, linear data structures like linked lists, stacks, queues, etc. can be used.

It is a dynamic DS and conveys a lot of information just by looking at the tree.

# Some common terminologies

node
edge
root
leaf node
parent node
child node
ansestor node
descendent node
degree of a node
degree of the tree
level of the tree
height of a node
height of the tree
depth of a node
size of a node

> **The root node is at level zero**

# Generic Tree(N-ary Tree)

Generic trees are a collection of nodes where each node is a data structure that consists of records and a list of references to its children(duplicate references are not allowed).

Unlike the linked list, each node stores the address of multiple nodes.

Every node stores address of its children and the very first node’s address will be stored in a separate pointer called root.

The Generic trees are the N-ary trees which have the following properties:

1. Many children at every node.

2. The number of nodes for each node is not known in advance.

## Properties of N-ary Tree

`L = (n-1)*I + 1` holds in any n-ary tree in which every node has either 0 or n children, where L is the number of leaf nodes and I is the number of internal nodes.

# Binary Tree

A tree is called binary tree if each node can have atmost two children.

Empty tree is also a valid binary tree.

Types of Binary tree

- **Strict Binary Tree**: A binary tree is called strict binary tree if each node has exactly two children or no children.
- **Full Binary Tree**: A binary tree is called full binary tree if each node has exactly two children and all leaf nodes are at the same level.
- **Complete Binary Tree**: A binary tree is called complete binary tree if all leaf nodes are at height h or h – 1 and also without any missing number in the sequence.

Properties of Binary Tree:

- The number of nodes n in a full binary tree is 2^(h+1) – 1.
- The number of nodes n in a complete binary tree is between 2^h(minimum) and 2^(h+1) – 1(maximum).
- The number of leaf nodes in a full binary tree is 2^h.
- The number of NULL links (wasted pointers) in a complete binary tree of n nodes is n + 1.
  In trees, the default flow is from parent to children and it is not mandatory to show directed branches.

## Binary Tree as an ADT

Basic Operations

- Inserting an element into a tree
- Deleting an element from a tree
- Searching for an element
- Traversing the tree

Auxiliary Operations

- Finding the size of the tree
- Finding the height of the tree
- Finding the level which has maximum sum
- Finding the least common ancestor (LCA) for a given pair of nodes, and many more.

## Application of Binary Tree

Expression trees are used in compilers.

Huffman coding trees that are used in data compression algorithms.

Binary Search Tree (BST), which supports search, insertion and deletion on a collection of items in O(logn) (average).

Priority Queue (PQ), which supports search and deletion of minimum (or maximum) on a collection of items in logarithmic time (in worst case).

## Traversals

The process of visiting all nodes of a tree is called tree traversal.

Tree traversal is like searching the tree, except that in traversal the goal is to move through the tree in a particular order.

All nodes are processed in the traversal but searching stops when the required node is found.

Traversals in tree can be Depth-first or Bredth-first.

- Preorder Traversal
- Inorder Traversal
- Postorder Traversal
- Bredth first Traversal (Level order traversal)

# Trie

Trie is a multiway tree and used to store collection of string/words.

The Trie data structure is an efficient information re-trie-val data structure.

The Trie data struture is used to efficiently search for a particular string key among a list of such keys. Using the trie, the lookup operation can be performed in time complexity of O(key_length).

They are faster but require huge memory for storing the strings.

- There are some improved tries representations called trie compression techniques. But, even with those techniques we can reduce the memory only at the leaves and not at the internal nodes.

## Trie as an ADT

Basic Operations

- Search
- Insert
- Delete

Auxillary Operations

- Prefix search
- Lexiographical Ordering of words

## Hashing VS Trie

|                       | Trie                       | Hashing                     |
| --------------------- | -------------------------- | --------------------------- |
| Search                | O(word_len) in worst case  | O(word_len) in average case |
| Insert                | O(word_len) in worst case  | O(word_len) in average case |
| Delete                | O(word_len) in worst case  | O(word_len) in average case |
| Prefix Search         | O(prefix_len + output_len) | Not Supported               |
| Lexiographic Ordering | O(output_len)              | Not Supported               |

## Applications of Trie

Prefix or Complete Searching
Suggestions
Autocomplete feature
