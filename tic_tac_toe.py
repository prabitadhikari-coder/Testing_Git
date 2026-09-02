"""
Criss Cross (Tic-Tac-Toe) with an AI opponent
-----------------------------------------------
You play 'X', the AI plays 'O'.
The AI uses the Minimax algorithm, so it never loses - the best
you can do is force a draw.

Run:
    python tic_tac_toe.py
"""

import math
import random

PLAYER = "X"
AI = "O"
EMPTY = " "


def new_board():
    return [EMPTY] * 9


def print_board(board):
    rows = [board[i:i + 3] for i in range(0, 9, 3)]
    print()
    for i, row in enumerate(rows):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()


def print_position_guide():
    guide = [str(i + 1) for i in range(9)]
    print("Positions are numbered like this:")
    print_board(guide)


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


def game_over(board):
    return winner(board) is not None or is_full(board)


def minimax(board, depth, is_maximizing):
    result = winner(board)
    if result == AI:
        return 10 - depth
    if result == PLAYER:
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = PLAYER
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(best_score, score)
        return best_score


def best_ai_move(board):
    # Play randomly on the very first AI move for some variety,
    # otherwise this is completely deterministic (and unbeatable).
    moves = available_moves(board)
    if len(moves) == 9:
        return random.choice(moves)

    best_score = -math.inf
    best_move = None
    for move in moves:
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def get_player_move(board):
    while True:
        raw = input("Your move (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number from 1 to 9.")
            continue
        pos = int(raw) - 1
        if pos not in range(9):
            print("Please enter a number from 1 to 9.")
            continue
        if board[pos] != EMPTY:
            print("That square is already taken. Try again.")
            continue
        return pos


def choose_who_goes_first():
    while True:
        choice = input("Do you want to go first? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please answer y or n.")


def play_game():
    print("=" * 40)
    print("   CRISS CROSS (Tic-Tac-Toe) vs AI")
    print("=" * 40)
    print_position_guide()

    board = new_board()
    player_turn = choose_who_goes_first()

    while not game_over(board):
        print_board(board)
        if player_turn:
            move = get_player_move(board)
            board[move] = PLAYER
        else:
            print("AI is thinking...")
            move = best_ai_move(board)
            board[move] = AI
            print(f"AI plays position {move + 1}.")
        player_turn = not player_turn

    print_board(board)
    result = winner(board)
    if result == PLAYER:
        print("You win! Well played.")
    elif result == AI:
        print("The AI wins. Better luck next time!")
    else:
        print("It's a draw!")


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
