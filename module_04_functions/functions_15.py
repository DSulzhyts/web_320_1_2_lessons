data_dict = {"v": 60, "t": 3}


def calculate_way(v, t):
    way = v * t
    return way


print(f"Распаковка словаря {calculate_way(**data_dict)}")
print(f"Распаковка словаря {calculate_way(v=60, t=3)}")

