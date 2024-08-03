from __future__ import annotations


class Facade:

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2, ):
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self):
        results = []
        results.append("Facade инициализирует подсистемы:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade приказывает подсистемам выполнить действие:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:

    def operation1(self):
        return "Subsystem1: Готова!"

    def operation_n(self):
        return "Subsystem1: Вперед!"


class Subsystem2:

    def operation1(self):
        return "Subsystem2: Подготовится!"

    def operation_z(self):
        return "Subsystem2: Огонь!"


def client_code(facade: Facade):
    print(facade.operation(), end="")


subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
client_code(facade)
