from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component):
        pass

    def remove(self, component: Component):
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):

    def operation(self):
        return "Leaf"


class Composite(Component):
    def __init__(self):
        self._children: List[Component] = []

    def add(self, component: Component):
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch ({'+'.join(results)})"


def client_code(component: Component):
    print(f"Результат: {component.operation()}", end='')


def client_code2(component1: Component, component2: Component):
    if component1.is_composite():
        component1.add(component2)
    print(f"Результат: {component1.operation()}", end='')


if __name__ == "__main__":
    simple = Leaf()
    print("Клиент: у меня простой компонент:")
    client_code(simple)
    print('\n')

    tree = Composite()

    branch_1 = Composite()
    branch_1.add(Leaf())
    branch_1.add(Leaf())

    branch_2 = Composite()
    branch_2.add(Leaf())

    tree.add(branch_1)
    tree.add(branch_2)

    print("Клиент: Теперь у меня компонентное дерево:")
    client_code(tree)
    print('\n')

    print("Клиент: Мне не нужно проверять классы компонентов, даже оперируя всем деревом")
    client_code2(tree, simple)
