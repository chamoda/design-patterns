from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self) -> float:
        pass


class Number(Expression):
    def __init__(self, value: float) -> None:
        self.value = value

    def interpret(self) -> float:
        return self.value


class Add(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()


class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret()


if __name__ == "__main__":
    expression: Expression = Subtract(Add(Number(68), Number(2)), Number(1))
    print(expression.interpret())
