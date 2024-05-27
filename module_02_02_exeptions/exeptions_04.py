try:
    amount = int(input("Введите количество полученных предметов: "))
    items_type = input("Введите тип полученных предметов в родительном падеже: ")
    parts_quantity = int(input("Введите на сколько частей вы хотите разбить поставку: "))
    amount_1_part = amount // parts_quantity
    amount_1_part_rest = amount % parts_quantity
except (ValueError, ZeroDivisionError):
    print("Получено некорректное значение")
finally:
    print("Программа завершила свою работу")
