from abc import ABC

from src.core.color import Color, WHITE, BLACK
from src.core.text import Text


class Message(ABC):
    def __int__(self, text: str, text_color: Color = BLACK, background: Color = WHITE):
        self.background: Color = background
        self.text: Text = Text(text)
        self.text.color = text_color
