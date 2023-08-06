from ygame.example.game_2048.game_2048 import Game2048
from ygame.tkinter.game_engine_tkinter import GameEngineTkinter


def main():
    GameEngineTkinter(Game2048()).initialize()


if __name__ == "__main__":
    main()
