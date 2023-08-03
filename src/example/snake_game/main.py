from src.example.snake_game.snake_game import SnakeGame
from src.tkinter.game_engine_tkinter import GameEngineTkinter


def main():
    GameEngineTkinter(SnakeGame()).initialize()


if __name__ == '__main__':
    main()
