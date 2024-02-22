from __future__ import annotations
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def accpet(self, visitor: Visitor) -> str:
        pass


class Dot(Shape):
    def __init__(self, identifier: int) -> None:
        self.identifier = identifier

    def draw(self):
        print(f"Drawing dot {self.identifier}")

    def accpet(self, visitor: Visitor) -> str:
        return visitor.visit_dot(self)


class Circle(Shape):
    def __init__(self, identifier: int) -> None:
        self.identifier = identifier

    def draw(self):
        print(f"Drawing circle {self.identifier}")

    def accpet(self, visitor: Visitor) -> str:
        return visitor.visit_circle(self)


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot: Dot) -> str:
        pass

    @abstractmethod
    def visit_circle(self, circle: Circle) -> str:
        pass


class XMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot):
        return f"<dot id='{dot.identifier}'></dot>"

    def visit_circle(self, circle: Circle):
        return f"<circle id='{circle.identifier}'></circle>"


if __name__ == "__main__":
    shapes = [Dot(1), Circle(2), Dot(3)]
    exportVisitor = XMLExportVisitor()
    for shape in shapes:
        print(shape.accpet(exportVisitor))
