# Criss Cross (Tic-Tac-Toe) vs AI

A simple command-line Tic-Tac-Toe game written in Python, where you play against
an AI opponent that never loses.

## Files

| File | Purpose |
|---|---|
| `tic_tac_toe.py` | The game itself. Run this to play. |
| `EXPLAINATION.md` | A beginner-friendly walkthrough of how the Python code and the AI logic work. |
| `README.md` | This file. |

## Requirements

- Python 3.7 or newer
- No external libraries needed (only the built-in `math` and `random` modules)

## How to Run

1. Make sure Python is installed:
   ```
   python --version
   ```
2. Navigate to the folder containing `tic_tac_toe.py`.
3. Run the game:
   ```
   python tic_tac_toe.py
   ```

## How to Play

1. When the game starts, you'll see a number guide showing positions 1–9:
   ```
    1 | 2 | 3
   ---+---+---
    4 | 5 | 6
   ---+---+---
    7 | 8 | 9
   ```
2. Choose whether you want to go first (`y`) or let the AI go first (`n`).
3. On your turn, type the number of the square you want to play (1–9) and press Enter.
4. The AI will automatically make its move after you.
5. The game ends when someone gets three in a row (horizontally, vertically,
   or diagonally) or when the board fills up with no winner (a draw).
6. After the game ends, you can choose to play again or quit.

## About the AI

The AI uses an algorithm called **Minimax**, which looks ahead through every
possible way the rest of the game could play out and picks the move that
gives it the best guaranteed outcome. Because of this, the AI plays perfectly:

- If you play perfectly too, the game will always end in a **draw**.
- If you make a mistake, the AI will find a way to **win**.

See `EXPLAINATION.md` for a full breakdown of how this works.

## Ideas for Extending This Project

- Add a difficulty setting where the AI sometimes plays randomly instead of optimally.
- Add a GUI using `tkinter` instead of the text-based console.
- Add a scoreboard that tracks wins/losses/draws across multiple games.
- Turn it into a two-player mode (human vs human).
