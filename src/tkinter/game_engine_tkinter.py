import tkinter as tk

from src.core.color import BLUE, Color
from src.core.game import Game
from src.core.game_engine import GameEngine
from src.tkinter.cell_tkinter import CellTkinter


class GameEngineTkinter(GameEngine):

    def __init__(self, game: Game):
        super().__init__(game)

        self.title = "Game Engine Tkinter!"

        self.grid: list[CellTkinter] = []
        self.grid_line_id = []
        self.message_id: int | None = None

        self.__root = tk.Tk()
        self.__canvas: tk.Canvas | None = None

    def initialize(self):
        super().initialize()

        self.__root.title(self.title)
        self.__root.mainloop()

    def __init_canvas(self):
        self.__canvas = tk.Canvas(self.__root, width=self.width_px, height=self.height_px, bg="white")
        self.__canvas.bind("<Button-1>", self.on_left_click)
        self.__canvas.bind("<Button-3>", self.on_right_click)
        self.__root.bind("<KeyPress>", self.on_key_press)
        self.__canvas.pack()

    def update_grid(self):
        if self.__canvas is None:
            self.__init_canvas()

        self.__canvas.delete("All")

        for y in range(self.height):
            for x in range(self.width):
                self.grid.append(CellTkinter(x, y))

    def draw_grid_line(self):
        for i in range(self.width):
            x = 0 + (self.cell_size_px * i)
            self.grid_line_id.append(
                self.__canvas.create_line(x, 0, x, self.height_px, fill=BLUE.value, width=2))

        for j in range(self.height):
            y = 0 + (self.cell_size_px * j)
            self.grid_line_id.append(
                self.__canvas.create_line(0, y, self.width_px, y, fill=BLUE.value, width=2))

    def remove_grid_line(self):
        self.__canvas.delete(*self.grid_line_id)

    def draw_cell_color(self, cell: CellTkinter, color: Color):
        self.remove_cell_color(cell)

        cell.color = color

        x1 = self.cell_size_px * cell.x
        x2 = (self.cell_size_px * cell.x) + self.cell_size_px
        y1 = self.cell_size_px * cell.y
        y2 = (self.cell_size_px * cell.y) + self.cell_size_px
        cell.canvas_rectangle = self.__canvas.create_rectangle(x1, y1, x2, y2, fill=cell.color.value)

    def remove_cell_color(self, cell: CellTkinter):
        if cell.canvas_rectangle is not None:
            self.__canvas.delete(cell.canvas_rectangle)

    def draw_cell_text(self, cell: CellTkinter, text: str):
        self.remove_cell_text(cell)

        cell.set_text(text)

        x = (self.cell_size_px * cell.x) + self.cell_size_px / 2
        y = (self.cell_size_px * cell.y) + self.cell_size_px / 2
        cell.canvas_text = self.__canvas.create_text(x, y,
                                                     text=cell.value.get_text(),
                                                     font=cell.value.get_font(),
                                                     fill=cell.value.get_color())

    def remove_cell_text(self, cell: CellTkinter):
        if cell.canvas_text is not None:
            self.__canvas.delete(cell.canvas_text)

    def draw_message(self, text: str):
        pass

    def remove_message(self):
        if self.message_id is not None:
            self.__canvas.delete(self.message_id)

    def on_turn(self):
        super().on_turn()

        if self.is_active_timer:
            self.__canvas.after(self.interval_ms_timer, self.on_turn)

    def on_left_click(self, event: tk.Event):
        self.game.on_left_click(event.x // self.cell_size_px,
                                event.y // self.cell_size_px)

    def on_right_click(self, event: tk.Event):
        self.game.on_right_click(event.x // self.cell_size_px,
                                 event.y // self.cell_size_px)

    def on_key_press(self, event: tk.Event):
        self.game.on_key_press(event.char, event.keycode)
