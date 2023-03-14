# Introduction

Ok so this module is about Algorithms and Algorithms goes well with Data Structures.
This particular introduction is about how DS and Algo can be applied in real life. So sit tight grab a cup of coffee and let's see how DS and Algo are applied in real life.

# Arrays and Matrices

- 2D arrays (as matrix), are used in image processing.
- To Store a raster graphics (1000 by 1000 pixels) as a bitmap.
- Your viewing screen is also a multidimensional array of pixels.
- In an online exam question paper numbering.
- Sudoku or Chess Board are 2D arrays.
- It is also used in speech processing, in which each speech signal is an array.
- Arrangement of leader-board of a game.
- Book titles in a Library Management Systems.
- Online ticket booking.
- Contacts on a cell phone.
- In geology, matrices are used for making seismic surveys.
- Used for plotting graphs, statistics, surveys, and also to do scientific studies and research in almost different fields.
- Matrices are also used in representing real-world data like the population of people, infant mortality rate, etc.
- Spam email detection.(String which is a character array)
- Plagiarism detection.(String which is a character array)

# Linked List

- Image viewer software uses a linked list to view the previous and the next images using the previous and next buttons.(Doubly Linked List)
- Web pages can be accessed using the previous and the next button in a browser.(Doubly Linked List)
- Music Players next, previous buttons uses doubly/circular linked list based on our preference.
- MS-Paint drawings and shapes are connected via a linked list on canvas.
- To keep the track of turns in a multi-player game, a circular linked list is used.
- Each of the lines of code in an IDE internally is a record on a doubly-linked list.
- Left/Right swipe on Tinder uses a doubly-linked list.
- Social media content “feeds”.
- Used for symbol table management in a designing compiler
- Used in switching between applications and programs (Alt + Tab) in the Operating system (implemented using Circular Linked List)
- Train coaches are connected to one another in a doubly-linked list fashion.
- It can be used to implement Stacks, Queues, Graphs, and Trees.

# Stacks(LIFO)

- Undo/Redo button/operation in word processors.
- Wearing/Removing Bangles.
- Pile of Dinner Plates.
- Stacked chairs.
- Changing wearables on a cold evening, first in, comes out at last.
- Last Hired, First Fired — which is typically utilized when a company reduces its workforce in an economic recession.
- Stack/Queue is used in the back and forward buttons of the web browser.
- Browser History of visited websites.
- Syntaxes in languages are parsed using stacks.
- Message logs and all messages you get are arranged in a stack.
- Call logs, E-mails, Google photos’ any gallery, YouTube downloads, Notifications ( latest appears first ).
- Java Virtual Machine.
- Recursion.
- Used in IDEs to check for proper parentheses matching.
- Evaluate an expression (i.e., parse).

# Queue(FIFO)

- In Escalators.
- Printer spooler.
- Sending emails.
- Car washes queue.
- Http1.1 Server while responding to requests.
- Operating System uses queues for process/task scheduling.(Priority Queue)
- Priority queues are used in file downloading operations in a browser.
- Stack/Queue is used in the back and forward buttons of the web browser.
- While switching multiple applications, windows uses a circular queue.
- A circular queue is used to maintain the playing sequence of multiple players in a game.
- A queue can be implemented in — Linked List-based Queue, Array-based Queue, Stack-based Queue.

# Graph

- Facebook(undirected graphs), Instagram(directed graphs), and all social media networking sites, every user is Node, use the graph to suggest friends.
- The GPS navigation system also uses shortest path APIs. Google Maps, Apple Maps, and Bing Maps.
- React’s virtual DOM uses graph data structures.
- MS Excel uses DAG (Directed Acyclic Graphs).
- Path Optimization Algorithms, BFS, DFS.
- Recommendation Engines.
- Scientific Computations.
- Flight Networks.
- Page ranking.

# Tree

- A decision-based algorithm is used in machine learning which works upon the algorithm of a tree.
- Databases also use B-Tree data structures for indexing.
- Domain Name Server (DNS) also uses tree structures.
- The file system of computer or mobile.
- Parsers(XML parser), Filesystem.
- Code Compression(zip).
- DOM in Html.
- Evaluate an expression (i.e., parse).
- Integral to compilers/automata theory.
- To store the possible moves in a chess game.
- To store the genealogy information of biological species.
- Used by JVM (Java Virtual Machine) to store Java objects.
- Posting questions on websites like Quora, the comments are a child of questions.
- It is used in parsers, filesystems, IP routing tables, data analysis, and data mining applications.
- 3D Game Engine.(BST)
- Computer Graphics Rendering.(BST)
- Used when there is frequent Insertion/Deletion and few searches.(Red-Black Tree)
- K -mean Clustering using red-black tree, Databases, Simple-minded database, searching words inside dictionaries, searching on the web.(Red-Black Tree)
- Process Scheduling in Linux.(Red-Black Tree)
- More Search and less Insertion/Deletion.(AVL Tree)
- Data Analysis and Data Mining and the applications which involve more searches.(AVL Tree)
- Fast full-text search, used in most word processors.(Suffix Tree)
- Dictionary application.(Trie)
- Autocomplete feature in searching.(Trie)
- Auto-completing the text and spells checking.(Trie)

# Hash Table(Dictionary)

- Data stored in databases is generally of the key-value format which is done through hash tables.
- Social network “feeds”.
- Every time we type something to be searched in google chrome or other browsers, it generates the desired output based on the principle of hashing.
- Message Digest, a function of cryptography also uses hashing for creating output in such a manner that reaching the original input from that generated output is almost next to impossible.
- In our computers we have various files stored in it, each file has two very crucial information that is, filename and file path, in order to make a connection between the filename to its corresponding file path hash tables are used.
- Password hashing.
- Used for fast data lookup — symbol table for compilers, database indexing, caches, Unique data representation.
- To store a set of fixed keywords that are referenced very frequently.

# Heap

- Systems concerned with security and embedded systems such as Linux Kernel uses Heap Sort because of the O( nlog(n) ).
- If we are stuck in finding the K-th smallest (or largest) value of a number then heaps can solve the problem in an easy and fast manner.
- Used by JVM (Java Virtual Machine) to store Java objects.

# Search

- Finding a word in a lexicographically-unsorted physical dictionary book.(LS)
- Searching data in Linked List.(LS)
- Finding Page Number in a book, e.g. — Target page number is 35, you open at page no. 15, it’s less, you move ahead and open 43, it is greater, you again move backward.(BS)

# Sort

- Order things by their value.
- Backend Databases (Merge Sort).
- Playing Cards with your friends (Insertion Sort).
- sort() — uses IntroSort (a hybrid of Quicksort, Heapsort, and Insertion Sort), Faster than qsort().

# Backtracking (Brute Force Algo)

- Suppose we are coding a chess-playing algorithm and at a certain point, the algorithm finds that a set of steps fails to win. In this situation, the algorithm will reverse back to the safe state and try another possible set of steps.
- Sudoku solver
- 2048 game
- N-Queen Problem

# DP (Optimization over plain reccursion)

A. Real-life examples

- In Google Maps to find the shortest path between the source and the series of destinations (one by one) out of the various available paths.
- In networking to transfer data from a sender to various receivers in a sequential manner.

B. Applications in Computer science

- Multi-stage graph
- Traveling salesman problem
- Largest common subsequence - to identify similar videos used by youtube
- Optimal search binary tree- to get optimized search results.
- Single source shortest path- Bellman-Ford Algorithm.
- Document Distance Algorithms- to identify the extent of similarity between two text documents used by Search engines like Google, Wikipedia, Quora, and other websites.

# Greedy Algorithms

- Dijkstra algorithm.
- Shopping on a tight budget but want to buy gifts for all family members.
- Prim’s and Kruskal’s algorithms are used for finding the minimum spanning trees.

# DIJKSTRA Algorithm

- Used in applications like Google Maps to find the shortest path in a graph.

# PRIM’S and KRUSKAL’S

- Used for finding the minimum spanning trees.
