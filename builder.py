from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self._parts: list[str] = []

    def add_part(self, part: str):
        self._parts.append(part)

    def __str__(self):
        return f"Product parts: {str(self._parts)}"


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> Car:
        pass

    @abstractmethod
    def add_part_a(self) -> None:
        pass

    @abstractmethod
    def add_part_b(self) -> None:
        pass


class SedanCarBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    def add_part_a(self) -> None:
        self._car.add_part("Part A Sedan")

    def add_part_b(self) -> None:
        self._car.add_part("Part B Sedan")

    @property
    def product(self) -> Car:
        return self._car


class CovertableCarBulider(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    def add_part_a(self) -> None:
        self._car.add_part("Part A Covertable")

    def add_part_b(self) -> None:
        self._car.add_part("Part B Cnovertable")

    @property
    def product(self) -> Car:
        return self._car


class Director:
    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    @property
    def builder(self) -> Builder:
        return self._builder

    def build_minimum_viable_product(self) -> None:
        self.builder.add_part_a()

    def build_featured_product(self) -> None:
        self.builder.add_part_a()
        self.builder.add_part_b()


if __name__ == "__main__":
    director = Director(SedanCarBuilder())
    director.build_minimum_viable_product()
    car1 = director.builder.product

    director = Director(CovertableCarBulider())
    director.build_featured_product()
    car2 = director.builder.product

    print(car1)
    print(car2)
