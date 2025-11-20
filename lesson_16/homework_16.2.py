from abc import ABC, abstractmethod
import math

class Figure(ABC):

    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius



class EquilateralTriangle(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.__side ** 2

    def perimeter(self):
        return 3 * self.__side



figures = [
    Square(4),
    Circle(3),
    EquilateralTriangle(5)
]

for fig in figures:
    print(f"{fig.__class__.__name__}:")
    print("  Площа:", round(fig.area(), 2))
    print("  Периметр:", round(fig.perimeter(), 2))
    print()
