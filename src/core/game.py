from abc import ABC, abstractmethod

from src.core.cell import Cell
from src.core.color import Color
from src.core.game_engine import GameEngine


class Game(ABC):

    def __init__(self):
        self.__game_engine: GameEngine | None = None

    def set_game_engine(self, game_engine: GameEngine):
        self.__game_engine = game_engine

    @abstractmethod
    def initialize(self):
        pass

    def set_title(self, title: str):
        self.__game_engine.title = title

    def set_screen_size(self, width: int, height: int):
        self.__game_engine.set_screen_size(width, height)

    def show_grid(self, flag: bool):
        self.__game_engine.show_grid(flag)

    def set_cell(self, x: int, y: int, color=None, text=None):
        self.__game_engine.set_cell(x, y, color=color, text=text)

    def get_cell_color(self, x: int, y: int) -> Color:
        cell: Cell = self.__game_engine.get_cell(self.__game_engine.get_index(x, y))
        return cell.color

    def get_cell_text(self, x: int, y: int) -> str:
        cell: Cell = self.__game_engine.get_cell(self.__game_engine.get_index(x, y))
        return cell.get_text()

    def set_turn_timer(self, interval_ms: int):
        self.__game_engine.set_turn_timer(interval_ms)

    def stop_turn_timer(self):
        self.__game_engine.stop_turn_timer()

    def on_turn(self, step: int):
        pass

    def on_left_click(self, x: int, y: int):
        pass

    def on_right_click(self, x: int, y: int):
        pass

    def on_key_press(self, char: str, keycode: int):
        pass
