# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from ygame.example.calculator_game.calculator_game import CalculatorGame
from ygame.tkinter.game_engine_tkinter import GameEngineTkinter


def main():
    GameEngineTkinter(CalculatorGame()).initialize()


if __name__ == "__main__":
    main()
