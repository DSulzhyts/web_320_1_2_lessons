class Human:

    def __init__(self, name=None, birth_date=None, phone=None, city=None, country=None):
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country

    def change_name(self, name=None):
        if not self.name:
            name = input("Введите ваше имя: ")
            if name.isalpha() is True:
                self.name = name
            else:
                return "Ошибка ввода"
        else:
            self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name}, {self.birth_date}, {self.phone}, {self.city}, {self.country}"


human_ivan = Human(birth_date="10.10.2000", phone="123456789", city='Moscow', country='Russia')
human_ivan.change_name()
print(human_ivan)
human_ivan.change_name("Петр")
print(human_ivan)
