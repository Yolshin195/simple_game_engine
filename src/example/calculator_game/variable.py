
class Variable:
    def __init__(self, x=None, y=None, value=None, color=None):
        self.__x = x
        self.__y = y
        self.__value = value
        self.__color = color

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def text(self):
        return self.__value

    @text.setter
    def text(self, text):
        self.__value = text

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
