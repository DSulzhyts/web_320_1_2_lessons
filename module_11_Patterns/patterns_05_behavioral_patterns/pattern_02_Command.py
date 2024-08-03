from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):

    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        print(f"SimpleCommand: смотри я могу делать простые вещи например показывать"
              f"({self._payload})")


class ComplexCommand(Command):

    def __init__(self, receiver: Receiver, a, b):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        print("ComplexCommand: Комплексные операции должны быть сделаны объектом Получателем")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:

    def do_something(self, a):
        print(f"\nReceiver: работаю над ({a})", end="")

    def do_something_else(self, b):
        print(f"\nReceiver: Еще работаю и над ({b})", end="")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self):
        print("Invoker: Кто-нибудь что нибудь-хочет сделать перед тем как я начну?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...делаю что-то очень важное...")

        print("Invoker: Кто-нибудь что-нибудь хочет сделать после того как я закончу?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


invoker = Invoker()
invoker.set_on_start(SimpleCommand("Say Hi!"))
receiver = Receiver()
invoker.set_on_finish(ComplexCommand(
    receiver, "Send email", "Save report"))

invoker.do_something_important()