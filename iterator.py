from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class WordsCollection(Iterable[Any]):
    def __init__(self, collection: list[Any]) -> None:
        self._collection = collection

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> ReverseOrderIterator:
        return ReverseOrderIterator(self)


class ReverseOrderIterator(Iterator[Any]):
    _position: int

    def __init__(self, collection: WordsCollection):
        self._collection = collection
        self._position = -1

    def __next__(self) -> WordsCollection:
        try:
            value = self._collection[self._position]
            self._position -= 1
        except IndexError:
            raise StopIteration()
        return value


if __name__ == "__main__":
    collection = WordsCollection(
        ["Arthur Dent", "Ford Prefect", "Trillian", "Zaphod Beeblebrox"]
    )

    iterator = ReverseOrderIterator(collection)
    for value in iterator:
        print(value)
