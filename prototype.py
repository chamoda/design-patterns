from typing_extensions import Self
import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    _x: int
    _y: int

    @abstractmethod
    def clone(self) -> Self:
        pass

    def __str__(self) -> str:
        return str(self.__dict__)


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        self._x = x
        self._y = y
        self._radius = radius

    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    circle1 = Circle(1, 2, 1)
    circle2 = circle1.clone()

    print(circle1)
    print(circle2)
