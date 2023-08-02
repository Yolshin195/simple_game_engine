
class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.value: list[list] = self.fill()

    def fill(self) -> list[list]:
        value = []
        for y in range(self.height):
            for x in range(self.width):
                value.append([x, y, None])

        return value

    def find_winning_combination(self) -> list[list]:
        for i in range(self.width):
            combination_row = self.value[ i *3:( i +1 ) *3]
            if self.is_winning_combination(combination_row):
                return combination_row

            combination_column = self.value[i::3]
            if self.is_winning_combination(combination_column):
                return combination_column

        combination_diagonal_right = self.value[::4]
        if self.is_winning_combination(combination_diagonal_right):
            return combination_diagonal_right

        combination_diagonal_left = self.value[2:7:2]
        if self.is_winning_combination(combination_diagonal_left):
            return combination_diagonal_left

        return list()

    @staticmethod
    def is_winning_combination(combination: list[list]) -> bool:
        combination = [cell[2] for cell in combination]
        return len(set(combination)) == 1 and not (None in combination)

    def set(self, x: int, y: int, label: str):
        self.value[self.__get_index(x, y)][2] = label

    def __get_index(self, x: int, y: int) -> int:
        return y * self.width + x
