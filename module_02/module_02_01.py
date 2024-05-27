# # example 1
# print("1 == 1:", 1 == 1)
# print("1 == 2:", 1 == 2)
# print("1 != 1:", 1 != 1)
# print("1 != 2:", 1 != 2)
# print("1 > 1:", 1 > 1)
# print("1 > 2:", 1 > 2)
# print("2 > 1:", 2 > 1)
# print("1 < 1:", 1 < 1)
# print("1 < 2:", 1 < 2)
# print("2 < 1:", 2 < 1)
# print("1 >= 1:", 1 >= 1)
# print("1 >= 2:", 1 >= 2)
# print("2 >= 1:", 2 >= 1)
# print("1 <= 1:", 1 <= 1)
# print("1 <= 2:", 1 <= 2)
# print("2 <= 1:", 2 <= 1)


# # example 2
# print(bool(""))  # строка
# print(bool([]))  # список
# print(bool(()))  # кортеж
# print(bool({}))  # множество/словарь
# print(bool(0))  # целое число
# print(bool(0.0))  # число с плавающей точкой
# print(bool(None))  # Ничто
# print(bool("IT Step Academy"))  # строка
# print(bool(["item_1", "item_2"]))  # список
# print(bool(("item_1", "item_2")))  # кортеж
# print(bool({"item_1", "item_2"}))  # множество
# print(bool({"key_1": "value_1", "key_2": "value_2"}))  # словарь
# print(bool(1))  # целое число
# print(bool(0.5))  # число с плавающей точкой
# print(bool(5))  # целое число
# print(bool(1.5))  # число с плавающей точкой


# example 3_1
competent = True
responsible = True
print(competent and responsible)

competent = True
responsible = False
print(competent and responsible)

# example 3_2
competent = True
responsible = True
print(competent or responsible)

competent = True
responsible = False
print(competent or responsible or responsible or responsible)

competent = False
responsible = False
print(competent or responsible)

# example 3_3
previously_fired = True
print(not previously_fired)

previously_fired = False
print(not previously_fired)

# example 4 time 6.00 - 23.59

time = int(input("Введите время в часах: ")) % 24
luggage = False
ticket = True
money = False

print(money or ticket and not luggage and time > 6)

print((money or ticket) and not luggage and time > 6)

print(not luggage and time > 6 and money or ticket)
