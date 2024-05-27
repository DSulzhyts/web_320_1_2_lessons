from module_02_02_exeptions.custom_exeptions.custom_exeptions import OnlyPositiveException

# class DegreeErrorException(Exception):
#     def __init__(self, *args, **kwargs):
#         pass
#
#
# class OnlyIntException(Exception):
#     def __init__(self, *args, **kwargs):
#         pass
#
#
# try:
#     num = float(input('Введите число: '))
#     deg = input('В какую степень в диапазоне 0-7 возвести число: ')
#     if "." in deg:
#         raise OnlyIntException("Степень должна быть только целым числом!")
#     else:
#         deg = int(deg)
#         if 0 <= deg <= 7:
#             pass
#         else:
#             raise DegreeErrorException
# except OnlyIntException as ex:
#     print(ex)
# except DegreeErrorException:
#     print("Степень должна быть в промежутке от 0 до 7 включительно!")
# except ValueError:
#     print("Вы ввели неверное значение, допустимы только числа!")
# else:
#     print(f"Число {num} в степени {deg} = {num ** deg}")
# finally:
#     print("Программа завершила свою работу!")

#
# tariffs = {
#     ('мтс', 'мтс'): 50,
#     ('мтс', 'билайн'): 100,
#     ('мтс', 'мегафон'): 150,
#     ('билайн', 'мтс'): 90,
#     ('билайн', 'билайн'): 60,
#     ('билайн', 'мегафон'): 140,
#     ('мегафон', 'мтс'): 180,
#     ('мегафон', 'билайн'): 200,
#     ('мегафон', 'мегафон'): 30
# }
#
# try:
#     time = int(input("Введите время разговора в минутах: "))
#     if time < 0:
#         raise OnlyPositiveException("Значение времени звонка не может быть меньше 0")
#     operator_a = input("Выберите оператора, с которого звоните (МТС, Билайн, Мегафон): ").lower().strip()
#     operator_b = input("Выберите оператора, на который звоните (МТС, Билайн, Мегафон): ").lower().strip()
#     cost = time * tariffs[(operator_a, operator_b)]
# except OnlyPositiveException as ex:
#     print(ex)
# except ValueError:
#     print("Ошибка значения! Время должно быть целым числом!")
# except KeyError:
#     print("Ошибка ключа! Введен не существующий оператор!")
# except:
#     print("Что-то пошло не так!")
# else:
#     print(f"Стоимость разговора составляет: {cost} рублей.")
# finally:
#     print("Программа завершила свою работу!")


# def some_func(data_1, data_2):
#     if type(data_1) is int and type(data_2) is int:
#         print(data_1 * data_2)
#     elif type(data_1) is str and type(data_2) is str:
#         print(data_1 + data_2)
#
#
# some_func(10, 5)
# some_func("слово1", "слово2")