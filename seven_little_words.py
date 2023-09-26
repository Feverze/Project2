"""Seven Little Words.

The game.
Author: Frankie Benedetto
Version: 12/12/22
Honor Code: TA's
"""
import sys
from game_info import GameInfo
from game_board import GameBoard


def main():
    """Its the main part of the code."""
    if len(sys.argv) < 2:
        print("Usage: python seven_little_words.py <game_file>")
        return
    try:
        game_info = GameInfo(sys.argv[1])
    except:
        print("Game file is incomplete")
        return
    game_board = GameBoard(game_info)
    game_board.set_visible(True)


if __name__ == "__main__":
    main()