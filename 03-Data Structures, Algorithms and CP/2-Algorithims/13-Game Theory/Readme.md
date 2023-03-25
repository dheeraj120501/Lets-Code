# Introduction

# Strict Dominance Stratergy

Strategy x strictly dominates strategy y for a player if x generates a greater payoff than y regardless of what the other players do.

- Strict dominance does not allow for equal payoffs. For example, suppose playing x and y both generated a payoff of 2 for an opposing strategy. Then x does not strictly dominate y.

## The Prisoner’s Dilemma

The prisoner’s dilemma is the most common introduction to new students of game theory.

Two criminals are detained. The police suspect them of having conspired on a major crime but only have evidence of a minor crime. To charge them for the greater crime, they need to elicit a confession.

To do this, they lock the criminals in separate interrogation chambers and offer each of them the following deal.

- If both keep quiet, then they will each spend a minimal time in jail.
- If one confesses while the other keeps quiet, the police will let the rat go free while throwing the book at the silent one.
- If both confess, the testimony is no longer necessary, and so both will be charged for the larger crime—though the time in jail will not be as bad getting the book thrown at them.

We solve the prisoner’s dilemma using the **strict dominance** solution concept.

Rational players never play strictly dominated strategies.

- In a prisoner’s dilemma, confessing strictly dominates keeping quiet for both players. Thus, we expect both players to confess.

- The outcome of the game is inefficient. Both players would be better off if they both kept quiet instead. However, each player’s individual interest is to confess if they know that the other player will keep quiet. As such, silence is unsustainable.

The conclusions of a game theory model produces are only as the assumptions built into it. Here, we assumed that players only wanted to minimize their own jail time.

# Iterated Elimination of Strictly Dominated Strategies

A strategy is strictly dominated if another strategy exists that always pays strictly more regardless of what other players are doing.

- Rational players will never use such strategies.

If we know our opponent has a strictly dominated strategy, we should reason that the opponent will never play that strategy. Internalizing that might make change what we want to do in the game.

In IESDS we remove strictly dominated strategies from a game matrix entirely.

- A reduced matrix will still give us all the necessary information we need to solve a game.
- We continue eliminating strictly dominated strategies from the reduced form, even if they were not strictly dominated in the original matrix.
- We call this process iterated elimination of strictly dominated strategies.
- If a single set of strategies remains after eliminating all strictly dominated strategies, then we have a prediction for the game’s outcome.

Iterated elimination of strictly dominated strategies cannot solve all games.

# Nash Equilibrium

In a pure strategy Nash equilibrium, all players take deterministic actions with no element of randomness.

A game is in Nash equilibrium when all players are playing best responses to what the other players are doing.

- Put differently, a Nash equilibrium is a set of strategies, one for each player, such that no player has incentive to change his or her strategy given what the other players are doing.
- Another way to think of a Nash equilibrium is as a law that no one would want to break even in the absence of an effective police force.

At least one Nash equilibrium exists for all finite games. This is known as Nash’s Theorem.

A game is finite if the number of players in the game is finite and the number of pure strategies each player has is finite.

- The stag hunt has two players, each of whom has two pure strategies. Therefore, it is a finite game.

There may or may not be a Nash equilibrium in infinite games.

Nash equilibria can be inefficient.

# Minimax Algorithm

Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally.

- Since this is a backtracking based algorithm, it tries all possible moves, then backtracks and makes a decision.

It is widely used in two player turn-based games such as Tic-Tac-Toe, Backgammon, Mancala, Chess, etc.

In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible.

Every board state has a value associated with it.

- In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value.
- If the minimizer has the upper hand in that board state then it will tend to be some negative value.

The values of the board are calculated by some heuristics which are unique for every type of game. It is done by Evaluation Function, sometimes also called a Heuristic Function.

- The basic idea behind the evaluation function is to give a high value for a board if the maximizer turn or a low value for the board if the minimizer turn.
- Example: let us consider X as the maximizer and O as the minimizer and we are given a board state if in that particular state X wins then the function gives +1 score, if O wins then the function gives -1 score and if it's a draw then it gives 0.

The Min-Max algorithm is complete. It will almost certainly find a solution (if one exists) in the finite search tree.

## Complexity Analysis

**Time complexity** : O(b^d) b is the branching factor and d is count of depth or ply of graph or tree.

**Space Complexity** : O(bd) where b is branching factor into d is maximum depth of tree similar to DFS.

## Alpha-Beta Pruning

Alpha-Beta pruning is not actually a new algorithm, but rather an optimization technique for the minimax algorithm reducing the computation time by a huge factor.

It cuts off branches in the game tree which need not be searched because there already exists a better move available.

This is important because there are many times when we can't evaluate till the end for eg, in case of Chess where are possibility is very large.

It is called Alpha-Beta pruning because it passes 2 extra parameters in the minimax function, namely alpha and beta.

- Alpha is the best value that the maximizer currently can guarantee at that level or above.
- Beta is the best value that the minimizer currently can guarantee at that level or below.

# Zobrist Hashing

Zobrist Hashing is a hashing function that is widely used in 2 player board games. It is the most common hashing function used in transposition table.

- Transposition tables basically store the evaluated values of previous board states, so that if they are encountered again we simply retrieve the stored value from the transposition table.

# Iterative Deepening

# Monte Carlo Tree Search

In computer science, Monte Carlo tree search (MCTS) is a heuristic search algorithm for some kinds of decision processes, most notably those employed in game play.

It uses probabilistic methods to find the seemingly best move, instead of heuristic analysis like Minimax.

Trust Network

Exploration and Exploitation
