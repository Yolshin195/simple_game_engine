from src.core.color import Color, BLACK


class CellText:
    def __init__(self, value: str):
        self.id: any = None
        self.font_name: str = "Helvetica"
        self.font_size: int = 20
        self.color: Color = BLACK
        self.value: str = value

    def get_font(self) -> tuple:
        return self.font_name, self.font_size

    def get_color(self) -> str:
        return self.color.value

    def get_text(self) -> str:
        return str(self.value)
