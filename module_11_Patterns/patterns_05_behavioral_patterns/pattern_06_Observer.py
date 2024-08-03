from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    _state = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer):
        print("Subject: добавился наблюдатель")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        print("Subject: уведомляю наблюдателей")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        print("\nSubject: Я делаю что-то важное...")
        self._state = randrange(0, 10)

        print(f"Subject: Мое состояние только что изменилось на: {self._state}")
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject):
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject._state < 3:
            print("ConcreteObserverA: Реакция на событие")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Реакция на событие")



subject = ConcreteSubject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.some_business_logic()
subject.some_business_logic()

subject.detach(observer_a)

subject.some_business_logic()