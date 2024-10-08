from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Создатель: тот же код создателя только что отработал с {product.operation()}"
        return result


class ConcreteCreator1(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Результат ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Результат ConcreteProduct2"


def client_code(creator: Creator) -> None:
    print(f"Я не знаю класса создателя, но он работает!\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("Приложение запущено с ConcreteCreator1!")
    client_code(ConcreteCreator1())
    print('\n')

    print("Приложение запущено с ConcreteCreator2!")
    client_code(ConcreteCreator2())


