# car_speed = 150
# motorcycle_speed = 130
#
# if car_speed > motorcycle_speed:
#     print("Автомобиль быстрее мотоцикла")
# elif car_speed < motorcycle_speed:
#     print("Мотоцикл быстрее автомобиля")
# else:
#     print("Скорости равны")


# flowers_amount = 3
#
# if flowers_amount > 2:
#     print("У тебя минимум 3 цветка.")
#     if flowers_amount < 5:
#         print("У тебя меньше 5 цветков.")
#
# if flowers_amount > 2:
#     print("У тебя минимум 3 цветка.")
# elif flowers_amount < 5:
#     print("У тебя меньше 5 цветков.")


account = abs(int(input("Введите сумму в копилке: ")))
# account = abs(account)

if account > 0:
    withdrawal = int(input("Сколько вы хотите взять? "))
    withdrawal = abs(withdrawal)
    if withdrawal < account:
        account -= withdrawal
        print(f"Вам выдано {withdrawal}")
        print(f"Остаток {account}")
    else:
        print(f"Вы попросили {withdrawal}, а на счете только {account}")
else:
    print("Денег в копилке нет")