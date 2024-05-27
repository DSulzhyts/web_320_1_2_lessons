data_list = [60, 2]
data_tuple = (50, 3)


def calculate_way(v, t):
    way = v * t
    return way


print(f"Распаковка списка {calculate_way(*data_list)}")
print(f"Распаковка кортежа {calculate_way(*data_tuple)}")