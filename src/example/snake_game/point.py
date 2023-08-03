from typing import Callable


class Point:
    def __init__(self, x=None, y=None, label=None, color=None):
        self.x = x
        self.y = y
        self.label = label
        self.color = color

    def __add__(self, other: 'Point'):
        self.x += other.x
        self.y += other.y

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        return iter((self.x, self.y, self.label, self.color))

    def draw(self, draw_func: Callable[['Point'], None]):
        draw_func(self)

        return self
