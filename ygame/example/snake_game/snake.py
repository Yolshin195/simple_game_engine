# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from typing import Callable

from ygame.core.color import BLACK
from ygame.example.snake_game.point import Point


class Snake:
    def __init__(self):
        self.direction: Point | None = None
        self.head: Point = self.create_head(3, 3)
        self.body: list[Point] = [
            self.create_body(3, 2),
            self.create_body(4, 2),
        ]

        self.remove: Point | None = None

    def __eq__(self, other: any) -> bool:
        if isinstance(other, Snake):
            return self.head in other.body

        if isinstance(other, Point):
            return self.head == other or other in self.body

        return False

    def move(self):
        if self.direction is None:
            return

        self.body.insert(0, self.create_body(self.head.x, self.head.y))
        self.remove = self.body.pop()

        self.head + self.direction

    def feed(self):
        self.body.append(self.remove)

    def draw(self, draw_func: Callable[['Point'], None], remove_func: Callable[['Point'], None] = None):
        if self.remove is not None:
            remove_func(self.remove)
            self.remove = None

        draw_func(self.head)
        for body in self.body:
            draw_func(body)

    def set_direction(self, direction):
        self.direction = direction

    @staticmethod
    def create_head(x: int, y: int) -> Point:
        return Point(x, y, "\U0001F440", color=BLACK)

    @staticmethod
    def create_body(x: int, y: int) -> Point:
        return Point(x, y, "\U0001F534", color=BLACK)
