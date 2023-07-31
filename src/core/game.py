from abc import ABC, abstractmethod

from src.core.color import Color
from src.core.cell import Cell


class Game(ABC):

    def __init__(self):
        self.title = "Game"
        self.is_game_running = False
        self.width = 3
        self.height = 3
        self.is_show_grid = True
        self.grid: list[Cell] = []

    def start(self):
        """
            Метод вызывается игровым движком
        :return:
        """
        self.initialize()
        self.is_game_running = True

    @abstractmethod
    def initialize(self):
        pass

    def set_screen_size(self, width: int, height: int):
        self.width = width
        self.height = height

        self.__init_grid()

    def show_grid(self, flag: bool):
        self.is_show_grid = flag

    def set_cell_by_index(self, index: int, color=None, text=None):
        if 0 <= index <= 9:
            cell = self.grid[index]
            cell.color = color
            cell.set_text(text)
        else:
            raise Exception("Вы вышли за границы игрового поля")

    def set_cell(self, x: int, y: int, color=None, text=None):
        cell = self.__get_cell(x, y)
        cell.color = color
        cell.set_text(text)

    def set_cell_text(self, x: int, y: int, text):
        self.__get_cell(x, y).set_text(text)

    def set_cell_color(self, x: int, y: int, color: Color):
        self.__get_cell(x, y).color = color

    def get_cell_color(self, x: int, y: int) -> Color:
        return self.__get_cell(x, y).color

    def on_mouse_click(self, x: int, y: int):
        pass

    def on_key_press(self, char: str, keycode: int):
        pass

    def __get_cell(self, x: int, y: int) -> Cell:
        if 0 <= x <= self.width and 0 <= y <= self.height:
            index = y * self.width + x
            return self.grid[index]
        else:
            raise Exception("Вы вышли за границы игрового поля")

    def __init_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid.append(Cell(x, y))
