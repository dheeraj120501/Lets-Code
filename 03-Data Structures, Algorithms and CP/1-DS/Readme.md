# Asymptotic Notation

Asymptotic notations are mathematical tools to represent the time complexity of algorithms for asymptotic analysis.

The following 3 asymptotic notations are mostly used to represent the time complexity of algorithms:

- Θ Notation (Average Case)
- Big O Notation (Worst Case)
- Ω Notation (Best Case)

When it comes to analyzing algorithms, the asymptotic analysis seems to be the best way possible to do so. This is because asymptotic analysis analyzes algorithms in terms of the input size. It checks how are the time and space growing in terms of the input size.

Most of the times, we do the worst case analysis to analyze algorithms. In the worst analysis, we guarantee an upper bound on the running time of an algorithm which is a good piece of information.

The average case analysis is not easy to do in most of the practical cases and it is rarely done. In the average case analysis, we must know (or predict) the mathematical distribution of all possible inputs.

The Best Case analysis is bogus. Guaranteeing a lower bound on an algorithm doesn't provide any information as in the worst case, an algorithm may take years to run.
