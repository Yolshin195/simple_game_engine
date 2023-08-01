from src.core.cell import Cell


class CellTkinter(Cell):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.canvas_rectangle = None
        self.canvas_text = None
