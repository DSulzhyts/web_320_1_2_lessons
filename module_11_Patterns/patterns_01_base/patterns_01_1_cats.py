class Sausage:
    def __init__(self):
        self.__energy = 1

    def give_energy(self):
        return self.__energy


class CatSausage:
    def __init__(self, name, energy=0):
        self.name = name
        self.energy = energy

    def play(self):
        if self.energy > 0:
            self.energy -= 1
            return "Кот играет!"
        else:
            return "Нужна сарделька!"

    def eat(self, obj):
        if isinstance(obj, Sausage):
            self.energy += obj.give_energy()
            return f"Кот получил {obj.give_energy()} энергии"
        else:
            return "Кот есть только сардельки"


sausage = Sausage()
cat_s = CatSausage('Том')
print(cat_s.play())
print(cat_s.eat(sausage))
print(cat_s.play())
print(cat_s.play())
print(cat_s.eat("Еда"))
print(cat_s.play())