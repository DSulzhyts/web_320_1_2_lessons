# # 2.1
#
# litres = input("Введите количество доставленной воды: ")
#
# if litres.isdigit() is True:
#     litres_int = int(litres)
#     if litres_int < 20_000:
#         print("Премии нет!")
#     elif 20_000 <= litres_int < 30_000:
#         print("Премия 10%")
#     else:
#         print("Премия 20%")
# else:
#     print("Введены неверные данные!")

# # 2.2
#
# time_input = int(input("Прошло секунда с начала дня? "))
# user_choice = input("Часы - 1/Минуты - 2/Секунды - 3? ")
# minutes_in_day = 24 * 60
# seconds_in_day = 24 * 60 * 60
#
# if user_choice == "1":
#     print(round(24 - time_input / 60 / 60, 2))
# elif user_choice == "2":
#     print(round(minutes_in_day - time_input / 60, 2))
# else:
#     print(seconds_in_day - time_input)

# # 2.3
# console_cost = float(input("Введите стоимость одной приставки: "))
# console_quantity = int(input("Введите количество: "))
#
# if console_quantity <= 5:
#     console_cost = console_cost - console_cost * 0.05
# elif 6 <= console_quantity <= 10:
#     console_cost = console_cost - console_cost * 0.1
# else:
#     console_cost = console_cost - console_cost * 0.2
#
# user_choice = input("Цена за штуку? - 1/Цена всей партии? - 2: ")
#
# if user_choice == "1":
#     print(f"Цена за штуку {console_cost}")
# elif user_choice == "2":
#     print(f"Цена все партии {console_cost * console_quantity}")
# else:
#     print("Неверный выбор!")

# # 2.5
#
# user_file = float(input("Введите объем файла в ГБ: "))
# user_speed = int(input("Введите скорость интернет соединения: "))
# user_file_bits = user_file * 1024 * 1024 * 1024 * 8
# user_choice = input("Часы - 1/Минуты - 2/Секунды - 3? ")
#
# if user_choice == "1":
#     time = user_file_bits / user_speed / 60 / 60
# elif user_choice == "2":
#     time = user_file_bits / user_speed / 60
# else:
#     time = user_file_bits / user_speed
#
# print(time)

# # 2.6
#
# user_time = int(input("Введите количество часов: "))
#
# if 0 <= user_time <= 24.00:
#     if 0 <= user_time < 6:
#         print("Night")
#     elif 6 <= user_time < 13:
#         print("Morning")
#     elif 13 <= user_time < 17:
#         print("Day")
#     else:
#         print("Evening")
# else:
#     print("Некорректный ввод в сутках 24 часа")


# #  2.8 012345
#
# user_num = input("Введите шестизначное число: ")
#
# if len(user_num) == 6 and user_num.isdigit() is True:
#     new_num = user_num[5] + user_num[4] + user_num[2] + user_num[3] + user_num[1] + user_num[0]
#     print(new_num)
# else:
#     print("Ошибка некорректный ввод данных!")

