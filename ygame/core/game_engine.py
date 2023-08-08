# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

from ygame.core.cell import Cell
from ygame.core.color import Color
from ygame.core.message import Message

if TYPE_CHECKING:
    from ygame.core.game import Game


class GameEngine(ABC):
    def __init__(self, game: 'Game'):
        self.game: 'Game' = game
        self.title = "Game Engine!"
        self.width = 3
        self.height = 3

        self.cell_size_px = 100
        self.width_px = 600
        self.height_px = 300

        self.grid: list[Cell] = []
        self.message: Message | None = None

        self.is_active_timer = False
        self.interval_ms_timer = 1000
        self.step_timer = 0

    def initialize(self):
        self.game.set_game_engine(self)
        self.game.initialize()

    def set_screen_size(self, width: int, height: int, cell_size_px=None):
        self.width = width
        self.height = height

        if cell_size_px is not None:
            self.cell_size_px = cell_size_px

        self.width_px = self.width * self.cell_size_px
        self.height_px = self.height * self.cell_size_px

        self.update_grid()

    def set_cell_size(self, size_px: int):
        self.cell_size_px = size_px

    def get_cell_size(self):
        return self.cell_size_px

    def show_grid(self, flag: bool):
        if flag:
            self.draw_grid_line()
        else:
            self.remove_grid_line()

    def set_cell(self, x: int, y: int, color: Color = None, text=None, text_color=None):
        cell = self.get_cell(self.get_index(x, y))
        if color is not None:
            self.draw_cell_color(cell, color)
        if text is not None:
            self.draw_cell_text(cell, text, text_color)

    def get_cell(self, index: int) -> Cell:
        return self.grid[index]

    def get_index(self, x: int, y: int) -> int:
        return y * self.width + x

    def update_grid(self):
        self.grid = []
        for y in range(self.height):
            for x in range(self.width):
                self.grid.append(Cell(x, y))

    def set_turn_timer(self, interval_ms: int):
        self.interval_ms_timer = interval_ms
        self.is_active_timer = True

        if self.step_timer == 0:
            self.on_turn()

    def stop_turn_timer(self):
        self.is_active_timer = False
        self.step_timer = 0

    @abstractmethod
    def draw_grid_line(self):
        pass

    @abstractmethod
    def remove_grid_line(self):
        pass

    @abstractmethod
    def draw_cell_color(self, cell: Cell, color: Color):
        pass

    @abstractmethod
    def remove_cell_color(self, cell: Cell):
        pass

    @abstractmethod
    def draw_cell_text(self, cell: Cell, text: str, text_color=None):
        pass

    @abstractmethod
    def remove_cell_text(self, cell: Cell):
        pass

    @abstractmethod
    def draw_message(self, text: str):
        pass

    @abstractmethod
    def remove_message(self):
        pass

    @abstractmethod
    def on_turn(self):
        """
        Must be added to the override function: super().on_turn()
        :return:
        """
        self.step_timer += 1
        self.game.on_turn(self.step_timer)

    @abstractmethod
    def on_left_click(self, event):
        """
        :example: self.game.on_left_click(event.x, event.y)
        :param event:
        :return:
        """

    @abstractmethod
    def on_right_click(self, event):
        """
        :example: self.game.on_right_click(event.x, event.y)
        :param event:
        :return:
        """

    @abstractmethod
    def on_key_press(self, event):
        """
        :example: self.game.on_key_press(event.char, event.keycode)
        :param event:
        :return:
        """
