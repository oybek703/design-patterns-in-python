from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    class PointFactory:
        @staticmethod
        def new_cartesian_point(x, y):
            point = Point(x, y)
            point.x = x
            point.y = y
            return point

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * cos(theta), theta * sin(theta))

    factory = PointFactory()


point1 = Point(2, 3)
point2 = Point.factory.new_polar_point(1, 2)
print(point1)
print(point2)
