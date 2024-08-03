from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler):
        self._next_handler = handler
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class MonkeyHandler(AbstractHandler):
    def handle(self, request):
        if request == "Банан":
            return f"Monkey: Я съем {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request):
        if request == "Орех":
            return f"Squirrel: Я съем {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request):
        if request == "Котлета":
            return f"Dog: Я съем {request}"
        else:
            return super().handle(request)


def client_code(hadler:Handler):
    for food in ["Орех", "Банан", "Чашка кофе"]:
        print(f"\nClient: Кто хочет {food}")
        result = hadler.handle(food)
        if result:
            print(f" {result}", end="")
        else:
            print(f" {food} осталась нетронутой", end="")


monkey = MonkeyHandler()
squirrel = SquirrelHandler()
dog = DogHandler()

dog.set_next(monkey).set_next(squirrel)
print("Цепочка: Обезьяна>Белка>Собака")
client_code(dog)
print("\n")

print("Подцепочка: Белка>Собака")
client_code(squirrel)
