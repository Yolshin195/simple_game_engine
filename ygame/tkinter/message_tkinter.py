# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from ygame.core.color import Color, BLACK, WHITE
from ygame.core.message import Message


class MessageTkinter(Message):

    def __init__(self, text: str, text_color: Color = BLACK, background: Color = WHITE):
        super().__int__(text, text_color, background)
        self.rectangle_id: int | None = None
        self.text_id: int | None = None
        self.remove_ms = 1000
