from custom_exeptions.custom_exeptions import OnlyPositiveException

while True:
    try:
        amount = int(input("Введите количество предметов: "))
        if amount < 0:
            raise OnlyPositiveException("У вас не может быть отрицательное количество предметов!!")
        items_type = input("Введите тип полученных предметов в родительном падеже: ")
        parts_quantity = int(input("Введите на сколько частей вы хотите разбить поставку: "))
        amount_1_part = amount // parts_quantity
        amount_1_part_rest = amount % parts_quantity
    except (ValueError, ZeroDivisionError):
        print("Получено некорректное значение")
    except OnlyPositiveException as ex_:
        print(ex_)
    except KeyboardInterrupt:
        print("Программа прервана по команде пользователя!")
    except:
        print("Что-то пошло не так!((")
    else:
        print(f"Поставка из {amount} {items_type} сохранена!")
        if amount_1_part_rest == 0:
            print(f"Каждая из {parts_quantity} частей состоит из {amount_1_part} {items_type}")
        else:
            print(f"Каждая из {parts_quantity} частей состоит из {amount_1_part} {items_type}")
            print(f"Нераспределенный остаток состоит из {amount_1_part_rest} {items_type}")
        break
    # finally:
    #     print("Программа завершила свою работу!")
