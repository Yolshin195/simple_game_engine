# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from ygame.core.color import RED
from ygame.example.snake_game.point import Point


class Apple(Point):
    def __init__(self, x, y):
        super().__init__(x, y, "\U0001F34E", RED)
