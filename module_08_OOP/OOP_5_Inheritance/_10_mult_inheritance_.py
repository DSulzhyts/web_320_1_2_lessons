class Wheels:

    # def __init__(self, radius):
    #     self.radius = radius
    @staticmethod
    def get_radius(radius):
        return f"Радиус колеса {radius}"


class Engine:

    # def __init__(self, val):
    #     self.val = val
    @staticmethod
    def get_value(val):
        return f"Двигатель объема {val}"


class Doors:

    # def __init__(self, quantity):
    #     self.quantity = quantity
    @staticmethod
    def get_quantity(quantity):
        return f"Количество дверей {quantity}"


class Car(Wheels, Engine, Doors):
    @staticmethod
    def display(wheels, value, quantity):
        print(Wheels.get_radius(wheels))
        print(Engine.get_value(value))
        print(Doors.get_quantity(quantity))


car = Car()
car.display(17, 2.0, 5)
