from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):

    @abstractmethod
    def useful_function_A(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_A(self) -> str:
        return "Результат продукт - А1 (гвозди - 20)"


class ConcreteProductA2(AbstractProductA):
    def useful_function_A(self) -> str:
        return "Результат продукт - А2 (гвозди - 40)"


class AbstractProductB(ABC):

    @abstractmethod
    def useful_function_B(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_function_B(self) -> str:
        return "Результат продукт - B1 (шурупы - 20)"

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_A()
        return f"Результат B1 в коллаборации с ({result}) (гвоздешуруп - 20)"


class ConcreteProductB2(AbstractProductB):
    def useful_function_B(self) -> str:
        return "Результат продукт - B2 (шурупы - 40)"

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_A()
        return f"Результат B2 в коллаборации с ({result}) (гвоздешуруп - 40)"


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_B()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end='')


if __name__ == "__main__":
    print("Клиент: Тестирование клиентского кода с первым типом фабрики:")
    client_code(ConcreteFactory1())

    print('\n')

    print("Клиент: Тестирование клиентского кода со вторым типом фабрики:")
    client_code(ConcreteFactory2())
