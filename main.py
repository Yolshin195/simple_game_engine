from src.example.simple_game import SimpleGame
from src.tkinter.game_engine_tkinter import GameEngineTkinter


def main():
    GameEngineTkinter(SimpleGame()).initialize()


if __name__ == '__main__':
    main()
