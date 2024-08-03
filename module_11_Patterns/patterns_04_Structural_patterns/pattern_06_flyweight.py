import json
from typing import Dict


class Flyweight:

    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Показываю общee ({s}) и уникальное ({u}) состояние.", end="")


class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state):
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Не могу найти легковес, создаю новый.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Реиспользуем существующий легковес")

        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print(f"FlyweightFactory: У меня {count} легковесов")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(factory: FlyweightFactory, plates, owner, brand, model, color):
    print("\n\nClient: Добавляем автомобиль в БД")
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])


factory = FlyweightFactory([
    ["Chevrolet", "Camaro2018", "pink"],
    ["Mercedes Benz", "C300", "black"],
    ["Mercedes Benz", "C500", "red"],
    ["BMW", "M5", "red"],
    ["BMW", "X6", "white"],
])

factory.list_flyweights()

add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")
add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "X1", "red")
print("\n")

factory.list_flyweights()