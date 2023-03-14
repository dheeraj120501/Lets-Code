# **Introduction to CP**

Competitive programming combines two topics:

- **Design of algorithms**
  - An algorithm for solving a problem has to be both correct and efficient, and the core of the problem is often about inventing an efficient algorithm.
  - A solution to a problem is a combination of well-known techniques and new insights.
- **Implementation of algorithms**
  - A good coding style in contests is straightforward and concise.

The benefits of using C++ are that it is a very efficient language and its standard library contains a large collection of data structures and algorithms.

Competitive programming is not about learning complex and obscure algorithms by heart, but rather about learning problem solving and ways to approach difficult problems using simple tools.

# **Gist of CPP**

Pre-processor directive is a feature of the g++ compiler.

- bit/stdc++.h is a header file that is supported by a few compilers that allows us to include the entire standard library. So, it is not needed to separately include libraries such as iostream, vector and algorithm, but rather they are available.

`g++ -std=c++11 -O2 -Wall test.cpp -o test`

- This command produces a binary file test from the source code test.cpp.
- The compiler follows the C++11 standard (-std=c++11), optimizes the code (-O2) and shows warnings about possible errors (-Wall).

# **Taking Inputs**

In most contests, standard streams are used for reading input and writing output.

In C++ `cin` is for input and `cout` is for output and this is done using streams.

- **Buffer**: A buffer is a temporary blog of memory used to temporarily store data while it is being moved from one place to another.
- Typically, the data is stored in a buffer as it is retrieved from an input device (such as a microphone) or just before it is sent to an output device (such as speakers).
- Flushing the buffer is the act of transferring the data from the buffer to the file.
- A buffer flush is the transfer of computer data from a temporary storage area to the computer’s permanent memory.
  - For instance, consider writing to a file. This is an expensive operation. If in your code you write one byte at a time, then each write of a byte is going to be very costly. So a common way to improve performance is to store the data that you are writing in a temporary buffer.
- Output buffers can be explicitly flushed to force the buffer to be written using flush.
- Generally, stdout/cout is line-buffered: the output doesn't get sent to the OS until you write a newline or explicitly flush the buffer.
- Also reading cin flushes cout which mean if a cout is present before cin then at cin the buffer will be flushed or cleared by outputting(not deleting) everything from the buffer.

The newline `\n` works faster than `endl`, because endl always causes a flush operation but while `endl` takes no extra space, `\n` being a character takes one byte.

- endl is slower because it forces a flushing stream, which is usually unnecessary. (You’d need to flush if you were writing, say, an interactive progress bar, but not when writing a million lines of data.)

`scanf` and `printf` are usually a bit faster, but they are also more difficult to use.

- Input and output is sometimes a bottleneck in the program.
- In order to get the same result with cin and cout use the following lines at the beginning of the main function:
  ```cpp
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  ```
- The first line toggles on or off the synchronization of all the C++ standard streams with their corresponding standard C streams if it is called before the program performs its first input or output operation.
- Adding `ios_base::sync_with_stdio (false);` (which is true by default) before any I/O operation avoids this synchronization.
- tie() is a method that simply guarantees the flushing of std::cout before std::cin accepts an input. This is useful for interactive console programs which require the console to be updated constantly but also slows down the program for large I/O. The NULL part just returns a NULL pointer not letting it flush the buffer.

`getline` function read a whole line from the input, possibly containing spaces.

- It takes the stream object, the string to read from and the delimitter(which character to end with by default it's newline).
- There are other ways to take inputs in cpp as well like `gets()`, `cin.getline()`, `cin.get()` etc.

If the amount of data is unknown use a loop which reads elements from the input one after another, until there is no more data available in the input:

```cpp
while (cin >> x) {
    // code
}
```

In some contest systems, files are used for input and output. An easy solution for this is to write the code as usual using standard streams, but add the following lines to the beginning of the code which makes the program reads the input from the file input.txt and writes the output to the file ”output.txt”:

```cpp
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
```

The C++ standard does not exactly specify the sizes of any types, and the bounds depend on the compiler and platform.

# **Integers**

- For integer values we have `int` that have 32 bits, `long long` that has 64 bits and gcc also provides a 128-bit type `__int128_t`.

  - int can store a number of magnitude about 10^9, while long long stores a number of magnitude about 10^18 and \_\_int128_t of magnitude 10^38.

- The suffix **LL** means that the type of the number is **long long**.

```cpp
long long x = 123456789123456789LL;
```

- Usually contest problems are set so that the type long long is enough.
- A common mistake when using the type long long is that the type int is still used somewhere in the code.

```cpp
int a = 123456789;
long long b = a*a;
cout << b << "\n"; // -1757895751
```

Even though the variable b is of type long long, both numbers in the expression a*a are of type int and the result is also of type int. Because of this, the variable b will contain a wrong result. The problem can be solved by changing the type of a to long long or by changing the expression to (long long)a*a.

- A signed number −x equals an unsigned number 2^n − x (n is the number of bits used to store that number).

# **Modular Arithematic**

- (a + b) mod m = (a mod m + b mod m) mod m
- (a − b) mod m = (a mod m − b mod m) mod m
- (a · b) mod m = (a mod m · b mod m) mod m
- This is used to counter the overflow problem, we can take the remainder after every operation and the numbers will never become too large.
- In C++ and other languages, the remainder of a negative number is either zero or negative. To make sure there are no negative remainders is to first calculate the remainder as usual and then add m if the result is negative:

  ```cpp
  x = x%m;
  if (x < 0) x += m;
  ```

  - This is only needed when there are subtractions in the code and the remainder may become negative.

- Modulus(%) operation only works with integers and characters.

# **Floating Point Numbers**

- In C++ floating point numbers are stored in data type `float`(4 byte = 32 bits ) and `double`(8 bytes = 64 bits).
- The usual floating point types in competitive programming are the 64-bit `double` and, as an extension in the g++ compiler, the 80-bit `long double`.

- A difficulty when using floating point numbers is that some numbers cannot be represented accurately as floating point numbers, and there will be rounding errors. This is called _floating point imprecission_. This is also seen in other languages as well because of the way the floating values are stored in the memory.
  ```cpp
  double x = 0.3*3+0.1;
  printf("%.20f\n", x); // 0.99999999999999988898
  ```
  - It is risky to compare floating point numbers with the `==` operator, because of precision errors.
  - To compare floating point numbers is to assume that two numbers are equal if the difference between them is less than ε, where ε is a small number.(ε = 10^−9)
  ```cpp
  if (abs(a-b) < e^-9) {
  // a and b are equal
  }
  ```
- While floating point numbers are inaccurate, integers up to a certain limit can still be represented accurately.

# **Shortening the code**

- Using the command `typedef` it is possible to give a shorter name to a datatype. It is used to give alias name to the datatype keyword.

  ```cpp
  typedef long long ll;
  ```

- **Modern way of giving types and alias name**: The syntax `using ll = long long;` is more modern.

  - For a simple type definition it does exactly the same as `typedef long long ll;`
  - But using supports template parameters, so the concept is more powerful.

  ```cpp
    template<typename T>
    using MyList = std::list<T, MyAlloc<T>>;

    MyList<Sometype> myList;
  ```

  - Since a _typedef does not support template parameters_ we would need to 'misuse' a struct, something like this:

  ```cpp
    template<typename T>
    struct MyList {
      typedef std::list<T, MyAlloc<T>> type;
    };

    MyList<Sometype>::type myList;
  ```

- Macro is another way it means that _certain strings in the code will be changed before the compilation_. In C++, macros are defined using the `#define` keyword.

- A macro can also have parameters which makes it possible to shorten loops and other structures.
  ```cpp
  #define F first
  #define S second
  #define PB push_back
  #define MP make_pair
  #define REP(i,a,b) for (int i = a; i <= b; i++)
  ```
- Macro is a preprocessor statement and is for the compiler so it doen't ends with a semicolon.

# **Some usefull fact**

- A useful property of logarithms is that logk(x) equals the number of times we have to divide x by k before we reach the number 1.
- The number of digits of an integer x in base b is logb(x) + 1.
  - eg. Representation of 123 in base 2 is 1111011 and log2(123)+1 = 7.
- Useful techniques to solve a problem are:
  - Iterative method
  - Reccursion & Backtracking
  - Bit manipulation

# Bit manipulation

- Bit operators are used for manipulating bits, like `&`, `|`, `~`, `^`, `>>`, `<<`.
- XOR is a very important operator and `a ^ a = 0`, `a ^ 0 = a`.
- The formula `~x = −x − 1`.
- `x & 1 = 0` if x is even, and `x & 1 = 1` if x is odd.
- x is divisible by 2^k exactly when `x & (2^k − 1) = 0`.
- `x | (1 << k)` sets the kth bit of x to 1 (sets the bit).
- `x & ~(1 << k)` sets the kth bit of x to zero (clears the bit).
- `x ^ (1 << k)` inverts the kth bit of x (toggles the bit).
- `x & (x − 1)` clears the right most set bit.
- `x & −x` clears all the bits, except for the right most set bit.
- `x | (x − 1)` inverts all the bits right to the right most set bit.
- A positive number x is a power of 2 exactly when `x & (x − 1) = 0`.
- One pitfall when using bit masks is that `1 << k` is always an int bit mask. An easy way to create a long long bit mask is `1LL << k`.
- Sets can be implemented and represented using bit manipulation.
  - Every subset of a set {0, 1, 2,..., n − 1} can be represented as an n bit integer whose one bits indicate which elements belong to the subset.
  - This is an efficient way to represent sets, because every element requires only one bit of memory, and set operations can be implemented as bit operations.
  - eg. as int is a 32-bit type, an int number can represent any subset of the set {0, 1, 2,..., 31}. The bit representation of the set {1, 3, 4, 8} is 00000000000000000000000100011010.
  - Union (a | b), Intersection (a & b), Complement (~a), Difference (a & (~b)).
- The C++ standard library also provides the bitset structure, which corresponds to an array whose each value is either 0 or 1 and each element has the size of 1 bit.

# **Time Complexity**

- The time complexity of an algorithm estimates how much time the algorithm will use for some input.
- A time complexity does not tell us the exact number of times the code is executed, but it only shows the order of magnitude.
- If the algorithm consists of consecutive phases, the total time complexity is the largest time complexity of a single phase.
  - For example, the following code consists of three phases with time complexities O(n), O(n^2) and O(n). Thus, the total time complexity is O(n^2).
- Sometimes the time complexity depends on several factors. In this case, the time complexity formula contains several variables.
  - But keep in mind that the complexity is always determined in terms of the input size n,m etc.
- The time complexity of a recursive function depends on the number of times the function is called and the time complexity of a single call. The total time complexity is the product of these values.
  - Time complexity of Reccursive function is calculated using Master theroem.
- Some common time complexities are **O(1) < O(log(n)) < O(root(n)) < O(n) < O(nlog(n)) < O(n^k) < O(k^n) < O(n!)**.
  - A polynomial time complexity roughly means that the algorithm is efficient, basically all the above time complexity except k^n and n!.
- Generally, while doing competitive programming problems on various sites, the most difficult task faced is writing the code under desired complexity otherwise the program will get a TLE ( Time Limit Exceeded ).
- Most of the sites these days allow 10^8 operations per second, only a few sites still allow 10^7 operations.
- So We have to just make sure that even in the worst case our time complexity shouldn't exceed 10^8 operations which can be found by putting the max constraint as the value of n in the time complexity of the program, this is called 10^8 operation rule.
- eg
  1. 1 <= N <= 10^3
  - For Case 1: A naive solution that is using two for-loops works as it gives us a complexity of O(N^2), which even in the worst case will perform 10^6 operations which are well under 10^8. Ofcourse O(N) and O(NlogN) is also acceptable in this case.
  2. 1 <= N <= 10^5
  - For Case 2: We have to think of a better solution than O(N^2), as in worst case, it will perform 10^10 operations as N is 10^5. So complexity acceptable for this case is either O(NlogN) which is approximately 10^6 (10^5 \* ~10) operations well under 10^8 or O(N).
  3. 1 <= N <= 10^8
  - For Case 3: Even O(NlogN) gives us TLE as it performs ~10^9 operations which are over 10^8. So the only solution which is acceptable is O(N) which in worst case will perform 10^8 operations.

![10^8 Operation Rule](./images/10^8_Operation_rule.webp "10^8 Operation Rule")

# Optimizing the code

- A C++ compiler converts C++ code into machine code that the processor can execute. An important task of the compiler is to optimize the code. The resulting machine code should correspond to the C++ code but also be as fast as possible.
- Compiler Explorer is an online tool that can be used to examine outputs of various compilers, including g++.
- It is often not necessary to use optimization tricks (like prefer bit operations to modulo and division) in C++, because the compiler also knows the tricks and can apply them.
- It can also detect unnecessary code and remove it(like tree shaking).

- **Compiler Specific Optimization**: This can be done by using -02 option in g++ compiler.

```cpp
void test(int n) {
  int s = 0;
  for (int i = 1; i <= n; i++) {
  s += i;
  }
}
```

- The corresponding assembly output is simply `ret` meaning that we return from the function. Since the value of s is not used, the variable and the loop can be removed and the code works in O(1) time.
- Thus when measuring the running time of a code, it is important that the result of the code is used (e.g., we can print it), so that the compiler cannot optimize away all the code.

- **Hardware Specific Optimization**: Some processors have special instructions that other processors do not have so by using hardware secific optimization we can optimize the code more.
  - The g++ flag `-march=native` turns on hardware-specific optimizations.
    - native means that the compiler automatically detects the actual architecture of the processor and uses hardware-specific optimizations if possible.
  - When processors execute code, they also try to do it as fast as possible. There are caches that speed up memory accesses, and it may also be possible to execute several instructions in parallel.
    - **Caches**: Using the main memory is relatively slow, processors have caches that contain small parts of the memory and can be accessed faster. The caches are automatically used when nearby memory contents are read or written.
    - **Parallelism**: Modern processors can execute multiple instructions at the same time, and this happens automatically in many situations. In general, two consecutive instructions can be executed in parallel if they do not depend on each other.

# Sorting

- Many efficient algorithms use sorting as a subroutine, because it is often easier to process data if the elements are in a sorted order.
- The efficient general sorting algorithms work in O(nlogn) time, and many algorithms that use sorting as a subroutine also have this time complexity.
- Inversion is a pair of array elements (array[a],array[b]) such that a < b and array[a] > array[b] i.e. the elements are in the wrong order.
  - For example, the array 1 2 2 6 3 5 9 8 has three inversions: (6,3), (6,5) and (9,8).
  - The number of inversions indicates how much work is needed to sort the array. An array is completely sorted when there are no inversions.
  - Swapping a pair of consecutive elements that are in the wrong order removes exactly one inversion from the array.
- It turns out that it is not possible to sort an array faster than in O(nlogn) time when we restrict ourselves to sorting algorithms that are based on comparing array elements.
- The lower bound `nlogn` does not apply to algorithms that do not compare array elements but use some other information.
  - An example of such an algorithm is counting sort that sorts an array in O(n) time assuming that every element in the array is an integer between 0...c and c = O(n).
- **Counting Sort**: The algorithm creates a bookkeeping array, whose indices are elements of the original array. The algorithm iterates through the original array and calculates how many times each element appears in the array.
  - eg. 1 3 6 9 9 3 5 9 makes the bookkeeping array of 1 0 2 0 1 1 0 0 3 because the value at position 3 in the bookkeeping array is 2, because the element 3 appears 2 times in the original array.
  - Construction of the bookkeeping array takes O(n) time. After this, the sorted array can be created in O(n) time because the number of occurrences of each element can be retrieved from the bookkeeping array. Thus, the total time complexity of counting sort is O(n).
  - But it can only be used when the constant c is small enough, so that the array elements can be used as indices in the bookkeeping array.
- The `sort(beginItr, endItr, compFn)` function of C++ takes a begin iterator and an end iterator then sorts the entire container. Making changes in the original container.
  - For the array it also takes the start and end pointer like `sort(a, a+n)`.
  - It also takes a comparision Function which is basically a boolean function for custom sorting.
  ```cpp
  bool comp(string a, string b) {
  if (a.size() != b.size()) return a.size() < b.size();
  return a < b;
  }
  ```
- The C++11 standard requires that the `sort` function works in O( nlogn ) time; the exact implementation depends on the compiler

# Data Structures

- A data structure is a way to store data in the memory of a computer.
- **Dynamic arrays**: A dynamic array is an array whose size can be changed during the execution of the program.

  - The most popular dynamic array in C++ is the **vector** structure, which can be used almost like an ordinary array.
  - The internal implementation of a vector uses an ordinary array. If the size of the vector increases and the array becomes too small, a new array of double the size is allocated and all the elements are moved to the new array.

  ```cpp
  vector<int> v;
  v.push_back(3); // [3]
  v.push_back(2); // [3,2]
  v.push_back(5); // [3,2,5]
  cout << v[0] << "\n"; // 3
  cout << v[1] << "\n"; // 2
  cout << v[2] << "\n"; // 5
  cout << v.size() << "\n"; // 3
  cout << v.capacity() << "\n"; // 4 (as a new array of double size in case we try to append in full array)
  for (auto x : v) {
    cout << x << "\n";
  }
  cout << v.back() << "\n"; // 5
  v.pop_back();
  cout << v.back() << "\n"; // 2
  vector<int> v = {2,4,2,5,1};
  // size 10, initial value 0
  vector<int> v(10);
  // size 10, initial value 5
  vector<int> v(10, 5);
  ```

  - The **string** structure is also a dynamic array that can be used almost like a vector.
  - In addition, there is special syntax for strings that is not available in other data structures.
  - The function `substr(k, x)` returns the substring that begins at position k and has length x, and the function `find(t)` finds the position of the first occurrence of a substring t.

  ```cpp
  string a = "hatti";
  string b = a+a; // for concatination
  cout << b << "\n"; // hattihatti
  b[5] = 'v';
  cout << b << "\n"; // hattivatti
  string c = b.substr(3,4);
  cout << c << "\n"; // tiva
  ```

- **Set Structure**: A set is a data structure that maintains a unique(An important property of sets is that all their elements are distinct.) collection of elements.

  - The basic operations of sets are element insertion, search and removal.
  - The C++ STL contains two set implementations: The structure _set_ is based on a _balanced binary tree_ and its operations work in O(logn) time. The structure _unordered_set_ uses _hashing_, and its operations work in O(1) time on average.
  - unordered_set is more efficient but set maintains the order in which the elements are entered and provide some extra functions as well.
  - A set can be used mostly like a vector, but it is not possible to access the elements using the [] notation.

  ```cpp
  set<int> s;
  s.insert(3);
  s.insert(2);
  s.insert(5);
  cout << s.count(3) << "\n"; // 1
  cout << s.count(4) << "\n"; // 0
  s.erase(3);
  s.insert(4);
  cout << s.count(3) << "\n"; // 0
  cout << s.count(4) << "\n"; // 1
  set<int> s = {2,5,6,8};
  cout << s.size() << "\n"; // 4
  for (auto x : s) {
  cout << x << "\n";
  }
  ```

  - C++ also contains the structures `multiset` and `unordered_multiset` that otherwise work like `set` and `unordered_set` but they can contain multiple instances of an element.

- **Map structure**: A map is a generalized array that consists of key-value pairs.

  - The keys in an ordinary array are always the consecutive integers 0,1,...,n−1, where n is the size of the array.
  - The keys in a map can be of any data type and they do not have to be consecutive values.
  - C++ STL contains 2 map implementations that correspond to the set implementations: the structure `map` is based on a `balanced binary tree` and accessing elements takes O(logn) time, while the structure `unordered_map` uses `hashing` and accessing elements takes O(1) time on average.

  ```cpp
  map<string,int> m;
  m["monkey"] = 4;
  m["banana"] = 3;
  m["harpsichord"] = 9;
  cout << m["banana"] << "\n"; // 3
  map<string,int> m;
  cout << m["aybabtu"] << "\n"; // 0, If the value of a key is requested but the map does not contain it, the key is automatically added to the map with a default value.
  ```

- **Bitset**: A bitset is an array whose each value is either 0 or 1.

  - The benefit of using bitsets is that they require less memory than ordinary arrays, because each element in a bitset only uses one bit of memory. For example, if n bits are stored in an int array, 32n bits of memory will be used, but a corresponding bitset only requires n bits of memory.
  - The values of a bitset can be efficiently manipulated using bit operators, which makes it possible to optimize algorithms using bit sets.

  ```cpp
  bitset<10> s;
  s[1] = 1;
  s[3] = 1;
  s[4] = 1;
  s[7] = 1;
  cout << s[4] << "\n"; // 1
  cout << s[5] << "\n"; // 0
  bitset<10> s(string("0010011010")); // from right to left
  cout << s[4] << "\n"; // 1
  cout << s[5] << "\n"; // 0
  bitset<10> s(string("0010011010"));
  cout << s.count() << "\n"; // 4 this counts number of set bit
  bitset<10> a(string("0010110110"));
  bitset<10> b(string("1011011000"));
  cout << (a&b) << "\n"; // 0010010000
  cout << (a|b) << "\n"; // 1011111110
  cout << (a^b) << "\n"; // 1001101110
  ```

- **Stack**: A stack is a data structure that provides two O(1) time operations: adding an element to the top, and removing an element from the top.

  - Stack is `LIFO` so it is only possible to access the top element of a stack.

  ```cpp
  stack<int> s;
  s.push(3);
  s.push(2);
  s.push(5);
  cout << s.top(); // 5
  s.pop();
  cout << s.top(); // 2
  ```

- **Queue**: A queue also provides two O(1) time operations: adding an element to the end of the queue, and removing the first element in the queue.

  - Queue is FIFO, It is only possible to access the first and last element of a queue.

  ```cpp
  queue<int> q;
  q.push(3);
  q.push(2);
  q.push(5);
  cout << q.front(); // 3
  q.pop();
  cout << q.front(); // 2
  ```

- **Deque**: A deque is a dynamic array whose size can be efficiently changed at both ends of the array.

  - A deque provides the functions `push_back`, `pop_back`, `push_front` and `pop_front` as it is a double ended queue.
  - The internal implementation of a deque is more complex than that of a vector, and for this reason, a deque is slower than a vector.

- **Priority Queue**: A priority queue maintains a set of elements. The supported operations are insertion and, depending on the type of the queue, retrieval and removal of either the minimum or maximum element.

  - Insertion and removal take O(logn) time, and retrieval takes O(1) time.
  - A priority queue is usually implemented using a `heap structure` that is much simpler than a `balanced binary tree` used in an ordered set.
  - By default, the elements in a C++ priority queue are sorted in decreasing order, and it is possible to find and remove the largest element in the queue.

- **Iterator**: An iterator is a variable that points to an element in a data structure.

  - Most common iterators are `.begin()`, `.end()`, `.rbegin()`, `.rend()`.

  ```cpp
  vector<int> v = {5,4,7,9,2};
  sort(v.begin(), v.end());
  reverse(v.begin(), v.end());
  random_shuffle(v.begin(), v.end());
  // These functions can also be used with an ordinary array. In this case, the functions are given pointers to the array instead of iterators.
  int a[] = {5,4,7,9,2};
  sort(a, a+n);
  reverse(a, a+n);
  random_shuffle(a, a+n);
  ```

  - Iterators are often used to access elements. Just like pointer `*` dereference operator is used to get the value stored.

  ```cpp
  // type::iterator i or auto i;
  set<int>::iterator it = s.begin();
  for (auto it = s.begin(); it != s.end(); it++) {
    cout << *it << "\n";
  }
  ```

- The g++ compiler also provides some data structures that are not part of the C++ standard library called **policy-based structures**.

- It is often possible to solve a problem using either data structures or sorting.

# Basic Tips for some problems

If input array is sorted then

- Binary search
- Two pointers

If asked for all permutations/subsets then

- Backtracking

If given a tree then

- DFS
- BFS

If given a graph then

- DFS
- BFS

If given a linked list then

- Two pointers

If recursion is banned then

- Stack

If must solve in-place then

- Swap corresponding values
- Store one or more different values in the same pointer

If asked for maximum/minimum subarray/subset/options then

- Dynamic programming

If asked for top/least K items then

- Heap
- QuickSelect

If asked for common strings then

- Map
- Trie

Else

- Map/Set for O(1) time & O(n) space
- Sort input for O(nlogn) time and O(1) space
