import tkinter as tk

from src.core.game import Game
from src.core.color import BLUE


class GameEngineTkinter:
    def __init__(self, game):
        self.__root = tk.Tk()
        self.__canvas: tk.Canvas | None = None
        self.__game: Game = game
        self.__cell_size = 100
        self.__width = 600
        self.__height = 300

    def initialize(self):
        self.__game.start()
        self.__root.title(self.__game.title)

        self.__width = self.__cell_size * self.__game.width
        self.__height = self.__cell_size * self.__game.height

        self.__canvas = tk.Canvas(self.__root, width=self.__width, height=self.__height, bg="white")
        self.__canvas.bind("<Button-1>", self.on_mouse_click)
        self.__root.bind("<KeyPress>", self.on_key_press)
        self.__canvas.pack()

        self.draw()

        self.__root.mainloop()

    def draw(self):
        self.__canvas.delete("all")
        self.draw_cell()
        self.draw_grid_line()

        if self.__game.is_game_running:
            self.__canvas.after(100, self.draw)

    def draw_cell(self):
        for cell in self.__game.grid:
            if cell.color is not None:
                x1 = self.__cell_size * cell.x
                x2 = (self.__cell_size * cell.x) + self.__cell_size
                y1 = self.__cell_size * cell.y
                y2 = (self.__cell_size * cell.y) + self.__cell_size
                self.__canvas.create_rectangle(x1, y1, x2, y2, fill=cell.color.value)

            if cell.value is not None:
                x = (self.__cell_size * cell.x) + self.__cell_size / 2
                y = (self.__cell_size * cell.y) + self.__cell_size / 2
                self.__canvas.create_text(x, y,
                                          text=cell.value.get_text(),
                                          font=cell.value.get_font(),
                                          fill=cell.value.get_color())

    def draw_grid_line(self):
        if self.__game.is_show_grid:
            for i in range(self.__game.width):
                x = 0 + (self.__cell_size * i)
                self.__canvas.create_line(x, 0, x, self.__height, fill=BLUE.value, width=2)

            for j in range(self.__game.height):
                y = 0 + (self.__cell_size * j)
                self.__canvas.create_line(0, y, self.__width, y, fill=BLUE.value, width=2)

    def on_mouse_click(self, event: tk.Event):
        self.__game.on_mouse_click(event.x // self.__cell_size,
                                   event.y // self.__cell_size)

    def on_key_press(self, event: tk.Event):
        self.__game.on_key_press(event.char, event.keycode)
