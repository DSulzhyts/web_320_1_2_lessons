from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class AlphabeticalOrderIterator(Iterator):
    _position = None
    _reverse = False

    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):

    def __init__(self, collection=None):
        self._collection = collection or []

    def __getitem__(self, index):
        return self._collection[index]

    def __iter__(self):
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any):
        self._collection.append(item)


collection = WordsCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print("Straight traversal:")
print("\n".join(collection))
print("")

print("Reverse traversal:")
print("\n".join(collection.get_reverse_iterator()), end="")
