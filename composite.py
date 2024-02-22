from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    _x: int
    _y: int

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def get_x(self) -> int:
        pass

    @abstractmethod
    def get_y(self) -> int:
        pass


class Dot(Shape):
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def move(self):
        self._x = self.get_x() + 1
        self._y = self.get_y() + 1

    def paint(self):
        print(f"Painting dot at x:{self._x} y:{self._y}")

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        self._x = x
        self._y = y
        self._radius = radius

    def move(self):
        self._x = self.get_x() + 1
        self._y = self.get_y() + 1

    def paint(self):
        print(f"Painting circle at x:{self._x} y:{self._y} with radius:{self._radius}")

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y


class CompoundShape(Shape):
    _children: List[Shape]

    def __init__(self, children: list[Shape]) -> None:
        self._children = children

    def get_x(self) -> int:
        if len(self._children) == 0:
            return 0
        self._x = self._children[0].get_x()
        for child in self._children:
            if child.get_x() < self._x:
                self._x = child.get_x()
        return self._x

    def get_y(self) -> int:
        if len(self._children) == 0:
            return 0
        self._y = self._children[0].get_y()
        for child in self._children:
            if child.get_y() < self._y:
                self._y = child.get_y()
        return self._y

    def move(self):
        for child in self._children:
            child.move()

    def paint(self):
        for child in self._children:
            child.paint()


if __name__ == "__main__":
    shapes = CompoundShape([Dot(1, 2), Circle(3, 4, 5)])
    print(shapes.get_x())
    print(shapes.get_y())
    shapes.paint()
