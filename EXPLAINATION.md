# How This Game Works: Python + AI Explained

This document walks through `tic_tac_toe.py` piece by piece, explaining both
the **Python concepts** used and the **AI logic** (Minimax) that powers the
computer opponent. It's written for someone who is comfortable with basic
programming ideas but new to game AI.

---

## Part 1: Representing the Board in Python

```python
def new_board():
    return [EMPTY] * 9
```

The 3x3 grid is stored as a simple Python **list of 9 items**, indexed 0–8:

```
 0 | 1 | 2
---+---+---
 3 | 4 | 5
---+---+---
 6 | 7 | 8
```

Each item in the list holds one of three values: `"X"`, `"O"`, or `" "`
(empty). This is a common trick in game programming — instead of a 2D grid,
you use a flat 1D list and calculate rows/columns/diagonals using fixed
index patterns. It's simpler to loop over and simpler to pass around than a
2D structure.

When we print the board, we slice the list into three rows of three:

```python
rows = [board[i:i + 3] for i in range(0, 9, 3)]
```

This is a **list comprehension** — a compact way to build a new list by
looping. It grabs indices `0:3`, `3:6`, and `6:9`, giving us three rows.

---

## Part 2: Checking for a Winner

```python
lines = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]
```

Rather than writing separate code to check every row, column, and diagonal,
we define all 8 possible winning "lines" as tuples of indices. Then we loop
through them and check: are all three squares in this line filled with the
same non-empty symbol? If yes, that symbol has won.

This pattern — **describe the rules as data, then loop over the data** — is
a very common and powerful programming technique. It keeps the logic short
and easy to change (e.g., adapting this for a 4x4 board would just mean
updating the `lines` list).

---

## Part 3: The AI — Why It Never Loses

This is the core of the "AI" in the game. It isn't a machine-learning model
or a neural network — it's a **search algorithm** called **Minimax**. It's
one of the oldest and most fundamental ideas in game-playing AI. It's the
ancestor of the algorithms used in early chess engines.

### The Core Idea

Tic-Tac-Toe is a small enough game that a computer can think through *every
possible way the rest of the game could unfold* before making a move. Minimax
does exactly that:

1. Imagine the AI makes a move.
2. Then imagine the opponent responds with their best possible move.
3. Then imagine the AI responds with *its* best move.
4. ...and so on, until the game ends (win, lose, or draw).
5. Work backward: assume both players always play their best move at every
   step, and score the very first move accordingly.

The name "Minimax" comes from the fact that:
- The AI is the **maximizing** player — it tries to get the highest score.
- The opponent is treated as the **minimizing** player — it's assumed they
  will always try to get the lowest score for the AI (i.e., play optimally
  against it).

### The Scoring System

```python
if result == AI:
    return 10 - depth
if result == PLAYER:
    return depth - 10
if is_full(board):
    return 0
```

Every finished game gets a score:
- **AI wins** → positive score (`10 - depth`)
- **Player wins** → negative score (`depth - 10`)
- **Draw** → `0`

`depth` is how many moves deep into the future this outcome is. Subtracting
`depth` means the AI prefers to **win sooner rather than later**, and
prefers to **lose later rather than sooner** (delaying a loss gives the
human more chances to make a mistake). This is a subtle but important
detail in Minimax implementations.

### The Recursive Function

```python
def minimax(board, depth, is_maximizing):
    ...
    for move in available_moves(board):
        board[move] = AI  # or PLAYER
        score = minimax(board, depth + 1, not is_maximizing)
        board[move] = EMPTY  # undo the move
        ...
```

This function calls **itself** — a technique called **recursion**. Here's
the process:

1. Try placing a symbol in an empty square.
2. Call `minimax` again on this new board state, imagining it's now the
   other player's turn.
3. That call does the same thing — tries every move, and calls `minimax`
   again — until the board is full or someone has won.
4. Once a game-ending state is reached, it returns a score (10, -10, or 0)
   instead of recursing further.
5. Each level "unwinds," picking the maximum score (if it's the AI's
   turn to move) or minimum score (if it's the opponent's turn) among its
   children's results, and passes that back up.

Notice the line `board[move] = EMPTY` right after the recursive call — this
"undoes" the imaginary move. This is called **backtracking**: the function
explores a possibility, then resets the board so it can try the next
possibility cleanly, without permanently altering the real board.

### Choosing the Best Move

```python
def best_ai_move(board):
    for move in moves:
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
```

This is one level up from `minimax` itself: for each available square, it
temporarily plays there, asks "if I play here, what's the best score
Minimax predicts?", then undoes the move and moves to the next candidate.
Whichever square produced the highest score is chosen as the AI's real
move.

### Why This Makes the AI Unbeatable

Because the game tree for Tic-Tac-Toe is small (at most 9! = 362,880
possible sequences, and far fewer after removing finished games early), the
computer can fully explore every outcome in a fraction of a second. Since it
always assumes the human will also play optimally and picks the move that
is best against that assumption, there is no sequence of moves a human can
make to beat it. The mathematically best a human can achieve is a **draw**.

This "brute-force but smart" approach only works because Tic-Tac-Toe is
small. Games like Chess or Go have far too many possible positions to fully
search this way — real game AI for those uses techniques like pruning
(skipping branches that can't matter — see below), heuristics (educated
guesses about how good a position is without finishing the search), and
increasingly, machine learning.

---

## Part 4: Other Python Concepts Used

- **Functions** (`def ...`) — each piece of logic (printing the board,
  checking for a winner, getting input) is broken into its own function.
  This makes the code easier to read, test, and reuse.
- **Loops and conditionals** (`for`, `if`) — used throughout to repeat
  actions and make decisions.
- **`while True` loops with `input()`** — used in `get_player_move` and
  `choose_who_goes_first` to keep asking the user for input until they give
  a valid answer. This is a common pattern for handling user input safely.
- **`math.inf`** — represents infinity, used as a starting point when
  searching for the maximum or minimum score, so that literally any real
  score will beat it on the first comparison.
- **`random.choice()`** — used only for the AI's very first move, purely to
  add some variety between games (since the first move doesn't affect
  whether the AI can be beaten).

---

## Where to Go Next

If you want to go deeper into game AI, here are natural next steps:

1. **Alpha-Beta Pruning** — an optimization of Minimax that skips exploring
   branches that can't possibly change the outcome, making it much faster
   for bigger games.
2. **Heuristic evaluation** — for games too large to fully search (like
   Chess), instead of playing every game to the end, the AI stops early and
   estimates how good a position looks using rules of thumb.
3. **Machine learning approaches** — modern game AI (like AlphaGo) combines
   search algorithms like Minimax with neural networks trained on huge
   numbers of games, allowing the AI to "intuit" good moves instead of
   calculating every possibility.
