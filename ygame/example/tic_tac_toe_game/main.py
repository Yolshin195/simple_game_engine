# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from ygame.example.tic_tac_toe_game.tic_tac_toe_game import TicTacToeGame
from ygame.tkinter.game_engine_tkinter import GameEngineTkinter


def main():
    GameEngineTkinter(TicTacToeGame()).initialize()


if __name__ == "__main__":
    main()
