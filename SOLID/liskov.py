class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height

    @property
    def area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, new_width):
        self._width = self._height = new_width

    @Rectangle.height.setter
    def height(self, new_height):
        self._height = self._width = new_height


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected area of rectangle {expected}, got {rc.area}')


rc1 = Rectangle(2, 3)
sq1 = Square(5)
use_it(rc1)
use_it(sq1)
