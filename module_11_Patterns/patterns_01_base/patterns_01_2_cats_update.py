class Sausage:
    def __init__(self):
        self.__energy = 1

    def give_energy(self):
        return self.__energy


class Chicken:
    def __init__(self):
        self.__energy = 2

    def give_energy(self):
        return self.__energy


class Food:
    def __init__(self, food: object):
        self.food = food

    def give_energy(self):
        return self.food.give_energy()


class CatSausage:
    def __init__(self, name, energy=0):
        self.name = name
        self.energy = energy

    def play(self):
        if self.energy > 0:
            self.energy -= 1
            return "Кот играет!"
        else:
            return "Нужна еда!"

    def eat(self, obj):
        if isinstance(obj, Food):
            self.energy += obj.give_energy()
            return f"Кот получил {obj.give_energy()} энергии"
        else:
            return "Кот есть только еду"


# sausage = Sausage()
# chicken = Chicken()
food_sausage = Food(Sausage())
food_chicken = Food(Chicken())

cat_f = CatSausage('Том')
print(cat_f.play())
print(cat_f.eat(food_sausage))
print(cat_f.play())
print(cat_f.play())
print(cat_f.eat("Еда"))
print(cat_f.eat(food_chicken))
print(cat_f.play())
