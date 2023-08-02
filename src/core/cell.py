from src.core.text import Text
from src.core.color import Color


class Cell:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.color: Color | None = None
        self.value: Text | None = None

    def set_text(self, value):
        if self.value:
            self.value.value = value
        else:
            self.value = Text(value)

    def get_text(self):
        return self.value
