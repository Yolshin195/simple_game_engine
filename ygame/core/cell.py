# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from ygame.core.text import Text
from ygame.core.color import Color


class Cell:
    def __init__(self, x: int, y: int, color: Color = None, text=None, color_text: Color = None):
        self.x: int = x
        self.y: int = y
        self.color: Color | None = None if color is None else color
        self.value: Text | None = None if text is None else self.set_text(text, color_text)

    def set_text(self, value, color=None):
        if self.value:
            self.value.value = value
            if color is not None:
                self.value.color = color
        else:
            self.value = Text(value, color)

    def get_text(self):
        return self.value
