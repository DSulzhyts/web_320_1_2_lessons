goods = {
    "HDD_Toshiba": 2000,
    "SSD_Samsung": 8000,
    "CPU_AMD_Rysen_7": 20000,
    "CPU_AMD_Rysen_5": 13000
}


my_goods = {}

while len(my_goods) < 3:
    my_choice = input("Выберете товар для покупки: ")

    if my_choice not in goods:
        print(f"Товара {my_choice} нет в магазине!")
        continue
    else:
        my_quantity = int(input("Введите количество приобретаемого товара: "))
        if my_quantity > 0:
            my_goods[my_choice] = goods[my_choice] * my_quantity
        else:
            continue

for key, value in my_goods.items():
    print(f"{key} {round(value / goods[key])} штук, стоимость {value}")
