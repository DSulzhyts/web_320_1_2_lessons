class CakeForm:

    def __init__(self, form, dough, *args):
        self.form = form
        self.dough = dough
        if not args:
            self.ingredient = []
        else:
            self.ingredient = list(args)
        # print(f"Я кекс в форме {self.form}, из теста {self.dough}")

    def make_dough(self):
        return f"Мы замешиваем тесто {self.dough}!"

    def make_form(self):
        return f"Мы выкладываем тесто в форму {self.form}"

    def add_ingredient(self, ingredient):
        self.ingredient.append(ingredient)

    def cook_cake(self, time=40):
        if self.ingredient:
            if time > 80:
                return f"За {time} минут, кексик из теста {self.dough} с {', '.join(self.ingredient)} сгорит!"
            return f"Мы выпекаем тесто {self.dough} c {', '.join(self.ingredient)} {time} минут"
        else:
            if time > 80:
                return f"За {time} минут, кексик из теста {self.dough} сгорит!"
            return f"Мы выпекаем тесто {self.dough} {time} минут"


cake_1 = CakeForm("круглая", "мучное", 'ром', 'марципан')
print(cake_1.dough)
print(cake_1.form)
print(cake_1.cook_cake())
cake_1.dough = "имбирное"
cake_1.form = "звездочка"
print(cake_1.cook_cake())
print(cake_1.make_form())


# print(cake_1.make_dough())
# print(cake_1.make_form())
# cake_1.add_ingredient('изюм')
# cake_1.add_ingredient('цукаты')
# print(cake_1.cook_cake())
# print()
cake_2 = CakeForm("квадратная", "овсяное")
# cake_2.add_ingredient('марципан')
# cake_2.add_ingredient('ром')
# print(cake_2.make_dough())
# print(cake_2.make_form())
# print(cake_2.cook_cake(100))
