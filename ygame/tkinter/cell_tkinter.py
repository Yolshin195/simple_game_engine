# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from ygame.core.cell import Cell
from ygame.core.color import Color


class CellTkinter(Cell):
    def __init__(self, x: int, y: int, color: Color = None, text=None, color_text: Color = None):
        super().__init__(x, y, color, text, color_text)
        self.canvas_rectangle = None
        self.canvas_text = None
