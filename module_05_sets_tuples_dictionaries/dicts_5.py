fruits = {
    "яблоки": 100,
    "груши": 200,
    "персики": 400
}

my_fruit = input("Выберите фрукт: ")
weight = float(input("Вес в граммах: "))

if my_fruit in fruits:
    price = fruits[my_fruit] * weight / 1000
    print(f"Стоимость: {price} рублей")
else:
    print("Таких фруктов нет в ассортименте!")
