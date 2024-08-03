from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters


class Originator:
    _state = None

    def __init__(self, state):
        print(f"Originator: Мое текущее состояние: {self._state}")

    def do_something(self):
        print(f"Originator: я делаю что-то важное")
        self._state = self._generate_random_string(30)
        print(f"Originator: Мое состояние изменилось на {self._state}")

    @staticmethod
    def _generate_random_string(length=10):
        return "".join(sample(ascii_letters, length))

    def save(self):
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.get_state()
        print(f"Originator: Мое состояние изменилось на {self._state}")


class Memento(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_date(self):
        pass


class ConcreteMemento(Memento):

    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_name(self):
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self):
        return self._date


class Caretaker:

    def __init__(self, originator: Originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        print("\nCaretaker: сохраняю состояние Originator")
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: вернул состояние к: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker: вот список Memento (снимков)")


originator = Originator("Super-duper-super-puper-super.")
caretaker = Caretaker(originator)

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

print()
caretaker.show_history()

print("\nClient: Now, let's rollback!\n")
caretaker.undo()

print("\nClient: Once more!\n")
caretaker.undo()
