from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def dettach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass


class ConreteSubject(Subject):
    _observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def dettach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverA updated")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverB updated")


if __name__ == "__main__":
    subject = ConreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)
    subject.notify()
