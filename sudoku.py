import argparse
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

# Global Variables
BOARDS = [0, 1, 2, 3]
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

# Need to inherit from Exception superclass
class SudokuError(Exception):
    """
    """
    def __init__(self, error):
        self.error = error
        raise self.error
    
# The Class for only the Sudoku Board
class SudokuBoard(object):
    """
    """
    def __init__(self, board_file):
        self.board = self.__create_board(board_file)

    # Create Private Method
    def __create_board(self, board_file):
        # A 2D Matrix or a list of list or defaultdict(list)
        # would be created
        board = []

        # Step 1 : Iterate over each row
        for row in board_file:
            row = row.strip()

            # Step 2 : Go through each column
            if len(row) != 9:
                board = []
                raise SudokuError("Must have exactly 9 rows.")
            
            # Add a list to each rows.
            board.append([])

            # Iterate over each character
            for c in row:
                # Raise error if character is not an integer
                if not c.isdigit():
                    raise SudokuError("Only digits from 0-9 are allowed to be characters.")
        # Check for 9 lines (Assert over it), raise error if not true

        # Return the fully constructed board
        return board

    
