from __future__ import annotations
from abc import ABC


class Mediator(ABC):

    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator, реагирует на А и вызывает соответствующие операции")
            self._component2.do_c()
        elif event == "D":
            print("Mediator, реагирует на D и вызывает соответствующие операции")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:

    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 делает A")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 делает B")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 делает C")
        self.mediator.notify(self, "C")

    def do_d(self):
        print("Component 2 делает D")
        self.mediator.notify(self, "D")


c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()

print("\n", end="")

print("Client triggers operation D.")
c2.do_d()