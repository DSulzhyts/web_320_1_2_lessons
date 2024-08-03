from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:

    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self):
        return f"Abstraction: Базовая операция с {self.implementation.operation_implementation()}"


class ExtendedAbstraction(Abstraction):

    def operation(self):
        return f"ExtendedAbstraction: расширили операцию с {self.implementation.operation_implementation()}"


class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self):
        pass


class ConcreteImplementationPlatform1(Implementation):
    def operation_implementation(self):
        return f"ConcreteImplementationPlatform1: это результат на Platform1"


class ConcreteImplementationPlatform2(Implementation):
    def operation_implementation(self):
        return f"ConcreteImplementationPlatform2: это результат на Platform2"


def client_code(abstraction: Abstraction):
    print(abstraction.operation(), end='')


if __name__ == "__main__":
    implementation_platform = ConcreteImplementationPlatform1()
    abstraction = Abstraction(implementation_platform)
    client_code(abstraction)

    print('\n')

    implementation_platform = ConcreteImplementationPlatform2()
    abstraction = ExtendedAbstraction(implementation_platform)
    client_code(abstraction)
