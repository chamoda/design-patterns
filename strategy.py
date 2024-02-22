from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass


class StrategyAdd(Strategy):
    def execute(self, a: int, b: int):
        return a + b


class StrategySubstract(Strategy):
    def execute(self, a: int, b: int):
        return a - b


class StrategyMultiplay(Strategy):
    def execute(self, a: int, b: int):
        return a * b


class Context:
    _strategy: Strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, a: int, b: int):
        return self._strategy.execute(a, b)


if __name__ == "__main__":
    context = Context()
    context.set_strategy(StrategyAdd())
    print(context.execute_strategy(68, 1))
    context.set_strategy(StrategySubstract())
    print(context.execute_strategy(70, 1))
