from src.core.color import Color, BLACK, WHITE
from src.core.message import Message


class MessageTkinter(Message):

    def __init__(self, text: str, text_color: Color = BLACK, background: Color = WHITE):
        super().__int__(text, text_color, background)
        self.rectangle_id: int | None = None
        self.text_id: int | None = None
        self.remove_ms = 1000
