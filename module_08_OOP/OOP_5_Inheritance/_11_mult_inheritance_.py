class Wheels:

    @staticmethod
    def size(radius):
        return f"Радиус колеса {radius}"


class Engine:

    @staticmethod
    def value(val):
        return f"Двигатель объема {val}"


class Doors:

    @staticmethod
    def quantity(quantity):
        return f"Количество дверей {quantity}"


class Car(Wheels, Engine, Doors):

    def __init__(self, wheels, engine, doors):
        self.wheels = wheels
        self.engine = engine
        self.doors = doors

    # def display(self, wheels=None, engine=None, doors=None):
    #     print(self.wheels.size(wheels))
    #     print(self.engine.value(engine))
    #     print(self.doors.quantity(doors))
    def display(self):
        print(self.size(self.wheels))
        print(self.value(self.engine))
        print(self.quantity(self.doors))


car = Car(17, 2.0, 5)

car.display()
