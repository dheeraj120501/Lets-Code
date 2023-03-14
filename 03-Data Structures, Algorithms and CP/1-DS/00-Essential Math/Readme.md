# Basic Concepts

## Principle of Mathematical Induction

## The Peano Axioms

The entire formalization of arithmetic is based on five fundamental axioms, called Peano axioms, which define properties of natural numbers.

- 0 is a natural number
- Every natural number has a successor, which is also a natural number
- 0 is not the successor of any natural number
- Different natural numbers have different successors
- If a set contains the number 0 and it also contains the successor of every number in S, then S contains every natural number. (By principal of mathematical induction)

## Fundamental Theorem Of Arithmetic And The Division Algorithm

The fundamental theorem of arithmetic states that any integer greater than 1 can be written as a product of prime numbers in a unique way (up to the ordering of prime factors in the product).

- It emerges out as a corollary to the Euclid's first theorem.

The division algorithm states that given two integers a,b (b != 0) there exist two unique integers q and r such that `a = bq + r`, `0 <= r < b` q is typically called **quotient**, whereas r is called **remainder**.

- If r = 0, we say that b divides a, and denote it as b|a.

## Euclid's Theorems

**Euclid's first theorem (Or Euclid's lemma)**: `p | ab => p|a or p | b`. A direct consequence of this is the fundamental theorem of arithmetic.

**Euclid's second theorem (usually simply referred as "Euclid's theorem")** : There are infinitely many primes. While it is true that there are infinitely many primes, it should also be remembered that there are arbitarily large gap between prime numbers.

- In other words, it is always possible to get a sequence of n consecutive composite numbers, given n.

## GCD, LCM, Bezout's Identity

`(a,b)` denotes the gcd of a and b while `[a,b]` denotes the lcm of a and b.

- `(a,b) * [a,b] = ab`: This gives a very fast way to calculate LCM of two numbers. But keep in mind of overflow when we code this to find LCM so we do `( a / gcd ( a, b ) ) * b` so that overflow is handled.

- `(n, n+1) = 1`

- `(a, a) = a`

- `(a, 0) = a`

- `(a,b) = (a−b,b)`

- The numbers a and b are called coprimes iff (a,b) = 1 , i.e. iff `[a,b] = ab`.

- If gcd(a,b) = d then (a/d, b/d) = 1.

The most common algorithm for finding the greatest common divisor of two numbers is the **Euclid's algorithm**. This is an extremely efficient algorithm, as the number of steps required in this algorithm is at most 5 times the number of digits of the smaller number.

- Euclidean Algorithm works on the principle `GCD(a,b)=GCD(b,a%b)`. Since GCD(b,a%b) is a smaller state, it is easier to find than the original. And of course, we can apply the principle to the smaller states repeatedly until the state becomes trivial. The two trivial states for GCD are GCD(a,a)=a and GCD(a,0)=a.

-The complexity of Euclidean Algorithm according to the answer is `O(logA+logB)`.

- This algorithm work correctly for non-negative inputs only but it can easily be extended to work with negative numbers. You need to either send the absolute value of the inputs to the algorithm or use the absolute value of the return value.

- If you try GCD(0,0) then you might get RTE due to division by zero but the correct answer is 0.

- There is also a builtin function in C++ for finding gcd. You can simply write `__gcd(a,b)` to find GCD(a,b).

The bezout's identity states that if d = (a,b) then there always exist integers x and y such that `ax+by = d`.

- `k=d` is the smallest positive integer for which `ax+by = k` has a solution with integral x and y.

Given a,b, Finding x and y, such that ax+by = d is done by extended Euclid's algorithm, which can be implemented in recursive as well as iterative styles.

## Prime Number Theroem

In number theory, the prime number theorem (PNT) describes the asymptotic distribution of the prime numbers among the positive integers. It formalizes the intuitive idea that primes become less common as they become larger by precisely quantifying the rate at which this occurs.

PNT provides us with an estimation for Prime-Counting Function (In mathematics, the prime-counting function is the function counting the number of prime numbers less than or equal to some real number x. It is denoted by pi(x)).

PNT provides us with an estimation for Prime-Counting Function. It states that: π(N)≈Nln(N). The accuracy of the estimation increase as N becomes larger.

We can use the theorem for complexity analysis.

## Properties of a Prime Number

Let n is a prime number. So, any power of n will only be divisible by lower or equal powers of n.

## Primality Test

A prime number is a positive number greater than 1 which has no positive divisor except for 1 and itself.

- O(N): Here we simply iterates over all values between 2 and N-1 and checks if it can divide N. It has a complexity of O(N). We can observe that, when i is greater than n/2, it will never divide n. Hence, we can optimize it a bit.

- O(√N): In order for A×B to be equal to N, any of them must be <= √N. Every divisor >= √N has a complementary divisor which is <= √N. This means that if we fail to find any divisor of N below √N then it is safe to assume we will not find any divisor above √N.

## Integer Factorization

The most commonly used algorithm for the integer factorization is the Sieve of Eratosthenes. It generates all prime up to N.

The algorithm has a runtime complexity of O(Nlog(logN))

If we need to factorize all numbers between 1 to N, this task can be done using a single run of this algorithm which says For every integer k between 1 to N, we can maintain a single pair - the smallest prime that divides k, and its highest power, say (p,a). The remaining prime factors of k are then same as that of k/(pa).

NOD (Number of Divisors) of N is always even except for when N is a perfect square. Because whenever N is perfect square, √N would be its divisor and it will form a pair with itself.

A Highly Composite Number (HCN) is a positive integer which has more divisors than any smaller positive integer i.e, if NOD(N)>NOD(i), where 0<i<N, then N is HCN.

- There are two properties of HCN and both of them are related to prime factorization.

  - First K Primes: The prime factorization of HCN will contain the first K consecutive primes. If it doesn’t, then we can replace the kth prime in factorization with a smaller prime and still have the same NOD.

  - Non-Increasing Power of Primes: Power of prime factors of HCN, i.e, a1,a2…ak will form a non-increasing sequence.

- Highly Composite Numbers are product of Primorials (Primorials are same as Factorials, but instead of natural number we multiply primes. p3=2×3×5 and p5=2×3×5×7×11)

## Linear Congruence Equations

The equations of the form ax ≡ b (mod n) where (x is an unknown integer ) are called linear congruences. This will have a solution if and only if there exists an integer x such that n | (ax-b), i.e. ax -b = ny for some integer y, or in other words ax + n(-y) = b.

If ax ≡ b (mod n) has a solution, then there is a unique solution mod (n/d). If this solution is denoted by x0, then there are exactly d solutions mod n, given by x0+ kn/d where 0 <= k < d.

## Chinese Remainder Theorem

In general, a system of linear congruences`x ≡ a1 (mod n1)`, `x ≡ a2 (mod n2)`, `x ≡ a3 (mod n3)` .... `x ≡ ak (mod nk)` where `(ni,nj) = 1` for every ni != nj has a unique solution modulo n where n = n1n2n3...nk.

## Facatorials

Factorials are extremely important. A factorial of N = (N)\*(N-1)\*(N-2)\*(N-3)...1. Factorials are used while computing nPr, nCr. They quickly grow very large and so they need extremely careful handling with large numbers, big integer representation etc.

## Sequences

There are some popular integer sequences. Some of them are based on recursive relations. The Master theorem is popularly used to understand the complexity and bounds with recurring relationships. Some popular integer relations are the Fibonacci Series, Lusas Numbers, Stern Diatomic Numbers, Lazy Carter, Padovan Numbers and polygonal numbers such as Pentagonal Numbers, Hexagonal Numbers.

# Common Formullas

- Check if a number is even `num % 2 == 0`
- Sum of 1 to N `1 + 2 + ... + (N - 1) + N = (N+1) * N/2`
- Sum of Geometric Progression `2^0 + 2^1 + 2^2 + 2^3 + ... 2^n = 2^(n+1) - 1`
- Permutations of N `N! / (N-K)!`
- Combinations of N `N! / (K! \* (N-K)!)`

# Tips

- When a question involves "whether a number is a multiple of X", the modulo operator would be useful.
- When dealing with floating point numbers, take note of rounding mistakes. Consider using epsilon comparisons instead of equality checks. E.g. abs(x - y) <= 1e-6 instead of x == y.
- If the question asks you to implement an operator such as power, square root or division and want it to be faster than O(n), some sort of doubling (fast exponentiation) or halving (binary search) is usually the approach to go.
- When comparing the distance between two points, using `dx^2 + dy^2` is sufficient. It is unnecessary to square root the value.

# Corner cases

- Check for and handle overflow/underflow if you are using a typed language like Java and C++.
- Division by 0: If code involves division or modulo, remember to check for division or modulo by 0 case.
- Multiplication by 1
- Negative numbers
- Floating point impression

# Fibonacci Numbers

Ratio of two consequtive fibonacci numbers keeps approaching golden ratio.

- Golden ratio is given by

- A lot of natural things follow golden ratio.

- Look at the visual depiction of golden ratio.

Bidet's Formulla

- Not used that much in computers due to floating point imprecision.

Fibonacci Encoding

- Every integer can be written as the sum of fibonacci numbers without using any fibonacci number more than once like in binary coding.

Matrix Form of Fibonacci Numbers

Cassini's Identity

Addition Rule

For every positive integer m, Fmn is a multiple of Fn.

Two consecutive fibonacci numbers are always co-primes.

GCD(Fm, Fn) = F(GCD(m,n)) given m,n>=1.

If Fm is a multiple of Fn, them m is also a multiple of n.

Pissano's Period
