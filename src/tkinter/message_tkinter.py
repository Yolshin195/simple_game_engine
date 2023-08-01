from src.core.message import Message


class MessageTkinter(Message):

    def __init__(self, x: int, y: int, text: str):
        super().__int__(x, y, text)
        self.__rectangle_id: int | None = None
        self.__text_id: int | None = None
