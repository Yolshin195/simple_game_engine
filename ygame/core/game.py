# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

import random
import time
from abc import ABC, abstractmethod

from ygame.core.cell import Cell
from ygame.core.color import Color
from ygame.core.game_engine import GameEngine


class Game(ABC):

    def __init__(self):
        self.__game_engine: GameEngine | None = None

        random.seed(time.time())

    def set_game_engine(self, game_engine: GameEngine):
        """
        Связывает игровой движок с текущей игрой.
        Этот метод вызывается игровым движком

        GameEngineTkinter(SimpleGame()).initialize()

        Args:
            game_engine (GameEngine): Игровой движок, который будет связан с игрой.
        """
        self.__game_engine = game_engine

    @abstractmethod
    def initialize(self):
        """
        Абстрактный метод. Инициализирует игру. Должен быть реализован в подклассах.
        """

    def set_title(self, title: str):
        """
           Устанавливает заголовок игры.

           Args:
               title (str): Заголовок игры.
        """
        self.__game_engine.title = title

    def set_screen_size(self, width: int, height: int, cell_size_px=None):
        """
        Устанавливает размер экрана игры.

        Args:
            width (int): Ширина экрана в пикселях.
            height (int): Высота экрана в пикселях.
            cell_size_px (Optional[int]): Размер ячейки в пикселях. По умолчанию 100px.
        """
        self.__game_engine.set_screen_size(width, height, cell_size_px)

    def show_grid(self, flag: bool):
        self.__game_engine.show_grid(flag)

    def show_message(self, text: str):
        self.__game_engine.draw_message(text)

    def set_cell(self, x: int, y: int, color=None, text=None, text_color=None):
        self.__game_engine.set_cell(x, y, color=color, text=text, text_color=text_color)

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
        """
        :param step: step counting starts from one
        :return: None
        """

    def on_left_click(self, x: int, y: int):
        pass

    def on_right_click(self, x: int, y: int):
        pass

    def on_key_press(self, char: str, keycode: int):
        pass

    @staticmethod
    def get_random_number(begin: int, end: int) -> int:
        """
        Возвращает случайное целое число включительно из заданного диапазона.

        Args:
            begin (int): Начальное значение диапазона.
            end (int): Конечное значение диапазона.

        Returns:
            int: Случайное целое число в диапазоне [begin, end].
        """
        return random.randint(begin, end)
