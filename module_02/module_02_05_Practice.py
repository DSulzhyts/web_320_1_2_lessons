# print("Введите 2 числа")
# num_1 = int(input())
# num_2 = int(input())
# user_choice = input("Введите действие 1 - сумма, 2 - разность, 3 - произведение, 4 - среднее арифметическое")
#
# if user_choice == "1":
#     print(f'Сумма {num_1 + num_2}')
# elif user_choice == "2":
#     print(f'Разность {num_1 - num_2}')
# elif user_choice == "3":
#     print(f'Произведение {num_1 * num_2}')
# elif user_choice == "4":
#     print(f'Среднее арифметическое {(num_1 + num_2) / 2}')
# else:
#     print("Неверный выбор!")
#
#
# account = int(input("Введите сумму на счете: "))
# account = abs(account)
# if account >= 500:
#     print("Средств достаточно")
# else:
#     print("Средств недостаточно")

#
# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))
# num_3 = int(input("Введите третье число: "))
#
#
# if num_2 > num_1:
#     num_1 = num_2
# if num_3 > num_1:
#     num_1 = num_3
#
# print(num_1)
#
# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))
# num_3 = int(input("Введите третье число: "))
#
# if num_1 > num_2 and num_1 > num_3:
#     print(num_1)
# elif num_2 > num_3:
#     print(num_2)
# else:
#     print(num_3)


# min_q, max_q = 40, 60
#
# x = float(input("Введите влажность"))
#
# if 40 < x < 60:
#     print("Влажность комфортная!")
# else:
#     print("Влажность НЕкомфортная!")


def convert_rating(stars):
    if stars == "*":
        return "Ужасно"
    elif stars == "**":
        return "Очень плохо"
    elif stars == "***":
        return "Средненько"
    elif stars == "****":
        return "Всё в порядке"
    elif stars == "*****":
        return "Прекрасная поездка!"
    else:
        return "Некорректный ввод"


stars = input("Введите количество звездочек: ")
result = convert_rating(stars)
print(result)
