from src.core.color import Color, BLACK


class Text:
    def __init__(self, value: str, color=None, font_size=20, font_name="Helvetica"):
        self.font_name: str = font_name
        self.font_size: int = font_size
        self.color: Color = BLACK if color is None else color
        self.value: str = value

    def get_font(self) -> tuple:
        return self.font_name, self.font_size

    def get_color(self) -> str:
        return self.color.value

    def get_text(self) -> str:
        return str(self.value)
