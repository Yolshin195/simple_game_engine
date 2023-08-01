from abc import ABC

from src.core.color import Color, BLACK
from src.core.text import Text


class Message(ABC):
    def __int__(self, x: int, y: int, text: str):
        self.x = x
        self.y = y
        self.width_px = 600
        self.height_px = 300
        self.color: Color = BLACK
        self.text: Text = Text(text)
