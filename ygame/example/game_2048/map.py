

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.value = [None] * (self.width * self.height)

    def is_empty(self, x: int, y: int):
        return self.get(x, y) is None

    def get(self, x: int, y: int, default=None):
        value = self.value[self.get_index(x, y)]
        return default if value is None else value

    def set(self, x, y, value) -> bool:
        if self.is_empty(x, y):
            self.value[self.get_index(x, y)] = value
            return True

        return False

    def get_index(self, x: int, y: int) -> int:
        return (self.width * y) + x

    def move_left(self):
        for y in range(self.height):
            new_value = [None] * self.width
            start = y * self.width
            end = start + self.width
            i: int = 0
            for v in self.value[start:end]:
                if v is not None:
                    new_value[i] = v
                    i += 1
            self.value[start:end] = new_value

    def merge_left(self):
        for y in range(self.height):
            for x in range(self.width - 1):
                i = self.get_index(x, y)
                if self.value[i] == self.value[i+1] and self.value[i] is not None:
                    self.value[i] *= 2
                    self.value[i+1] = None

    def move_right(self):
        for y in range(self.height):
            new_value = [None] * self.width
            start = y * self.width
            end = start + self.width
            i: int = self.width - 1  # Начинаем с последнего индекса нового массива
            for v in reversed(self.value[start:end]):  # Итерируем в обратном порядке
                if v is not None:
                    new_value[i] = v
                    i -= 1
            self.value[start:end] = new_value

    def merge_right(self):
        for y in range(self.height):
            for x in range(self.width - 1, 0, -1):  # Идем в обратном порядке, начиная с последнего столбца
                i = self.get_index(x, y)
                if self.value[i] == self.value[i - 1] and self.value[i] is not None:
                    self.value[i] *= 2
                    self.value[i - 1] = None

    def move_up(self):
        for x in range(self.width):
            new_value = [None] * self.height
            i: int = 0
            for y in range(self.height):
                index = self.get_index(x, y)
                if self.value[index] is not None:
                    new_value[i] = self.value[index]
                    i += 1
            for y in range(self.height):
                index = self.get_index(x, y)
                self.value[index] = new_value[y]

    def merge_up(self):
        for x in range(self.width):
            for y in range(self.height - 1):
                i = self.get_index(x, y)
                if self.value[i] == self.value[i + self.width] and self.value[i] is not None:
                    self.value[i] *= 2
                    self.value[i + self.width] = None

    def move_down(self):
        for x in range(self.width):
            new_value = [None] * self.height
            i: int = self.height - 1
            for y in range(self.height - 1, -1, -1):
                index = self.get_index(x, y)
                if self.value[index] is not None:
                    new_value[i] = self.value[index]
                    i -= 1
            for y in range(self.height - 1, -1, -1):
                index = self.get_index(x, y)
                self.value[index] = new_value[y]

    def merge_down(self):
        for x in range(self.width):
            for y in range(self.height - 1, 0, -1):
                i = self.get_index(x, y)
                if self.value[i] == self.value[i - self.width] and self.value[i] is not None:
                    self.value[i] *= 2
                    self.value[i - self.width] = None
