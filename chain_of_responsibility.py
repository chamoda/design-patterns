from __future__ import annotations
from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: str) -> str | None:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> str | None:
        if self._next_handler:
            return self._next_handler.handle(request)


class MonkeyHandler(AbstractHandler):
    def handle(self, request: str) -> str | None:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: str) -> str | None:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: str) -> str | None:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)
    print(monkey.handle("Banana"))
    print(monkey.handle("Nut"))
    print(monkey.handle("MeatBall"))
