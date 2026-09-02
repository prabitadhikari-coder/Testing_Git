"""Custom exceptions for the Tic-Tac-Toe game."""


class TicTacToeError(Exception):
    """Base exception for the game."""


class BoardError(TicTacToeError):
    """Raised when the board is invalid."""


class InputInterruptedError(TicTacToeError):
    """Raised when the user interrupts input or the input stream ends."""


def validate_board(board):
    """Check that the board is a valid 9-cell list."""
    if not isinstance(board, list):
        raise BoardError("Board must be a list.")
    if len(board) != 9:
        raise BoardError("Board must contain exactly 9 positions.")

    valid_cells = {" ", "X", "O"}
    for index, cell in enumerate(board):
        if cell not in valid_cells:
            raise BoardError(f"Board contains an invalid value at position {index}: {cell!r}")
    return True

