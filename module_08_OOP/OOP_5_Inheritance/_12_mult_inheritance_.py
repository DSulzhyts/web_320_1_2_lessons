class Pet:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}."

    def get_sound(self):
        print(f"Издает звук ..", end=" ")

    def get_type(self):
        print(f"Это ", end=" ")


class Dog(Pet):
    def __init__(self, name, age, gender, sound, type_pet):
        super().__init__(name, age, gender)
        self.sound = sound
        self.type_pet = type_pet

    def get_sound(self):
        super().get_sound()
        print(self.sound)

    def get_type(self):
        super().get_type()
        print(self.type_pet)


dog1 = Dog("Тузик", "5", "Кабель", "Гав-Гав", "Дворянин")
print(dog1)
dog1.get_sound()
dog1.get_type()

