from __future__ import annotations
from typing import Any


class SingletonMeta(type):
    _instances: dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwargs: dict[str, Any]) -> Singleton:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"x: {self._x} y: {self._y}"


if __name__ == "__main__":
    s1 = Singleton(1, 2)
    s2 = Singleton(3, 4)
    print(id(s1) == id(s2))
    print(s1)
    print(s2)
