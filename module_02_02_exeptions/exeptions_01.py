while True:
    try:
        amount = int(input("Введите количество полученных предметов: "))
        items_type = input("Введите тип полученных предметов в родительном падеже: ")
        parts_quantity = int(input("Введите на сколько частей вы хотите разбить поставку: "))
        amount_1_part = amount // parts_quantity
        amount_1_part_rest = amount % parts_quantity
    except ValueError:
        print("Количество должно быть целым числом (int)")
    except ZeroDivisionError:
        print("Невозможно разбить поставку на 0 частей")
    else:
        print(f"Поставка из {amount} {items_type} сохранена!")
        if amount_1_part_rest == 0:
            print(f"Каждая из {parts_quantity} частей состоит из {amount_1_part} {items_type}")
        else:
            print(f"Каждая из {parts_quantity} частей состоит из {amount_1_part} {items_type}")
            print(f"Нераспределенный остаток состоит из {amount_1_part_rest} {items_type}")
    finally:
        print("Программа завершила свою работу")

