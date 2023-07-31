from src.core.game_engine_tkinter import GameEngineTkinter
from src.example.simple_game import SimpleGame
from src.example.tic_tac_toe_game import TicTacToeGame


def main():
    GameEngineTkinter(TicTacToeGame()).initialize()


if __name__ == '__main__':
    main()
