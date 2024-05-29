class CakeForm:

    def make_dough(self):
        return f"Мы замешиваем тесто!"

    def make_form(self):
        return f"Мы выкладываем тесто в форму"

    def cook_cake(self, time=40):
        if time > 80:
            return f"За {time} минут, кексик сгорит!"
        return f"Мы выпекаем тесто {time} минут"


cake_1 = CakeForm()
cake_2 = CakeForm()

print(cake_1.make_dough())
print(cake_1.make_form())
print(cake_1.cook_cake())
print()
print(cake_2.make_dough())
print(cake_2.make_form())
print(cake_2.cook_cake(100))
