class Confectionary:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(f"{self.name} по цене {self.price} руб/кг")


class Cake(Confectionary):

    def describe(self):
        print(f"{self.name} торт цена {self.price} руб/шт")


class Candy(Confectionary):

    def describe(self):
        print(f"{self.name} конфеты по цене {self.price} руб/кг")


class Cookie(Confectionary):
    pass


conf = Confectionary("Зефир", 600)
conf.describe()

cake = Cake("Венский", 1100)
cake.describe()

candy = Candy("Слива в шоколаде", 1500)
candy.describe()

cookie = Cookie("Овсяное", 400)
cookie.describe()
