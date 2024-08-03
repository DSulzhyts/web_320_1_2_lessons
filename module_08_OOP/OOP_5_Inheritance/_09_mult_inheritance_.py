class Item:

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price}"


class KBLanguageMixin:
    __language = "EN"

    def change_language(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    def get_language(self):
        return self.__language


class Keyboard(KBLanguageMixin, Item):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language


keyboard = Keyboard('Dark Project KD87A', 9600, 5)
print(keyboard)
print(keyboard.get_language())
keyboard.change_language()
print(keyboard.get_language())
