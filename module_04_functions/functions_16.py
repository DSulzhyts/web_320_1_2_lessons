data_list = [60, 2]
data_dict = {"v_d": 60, "t_d": 3}


def calculate_way(v_l, t_l, v_d, t_d):
    way_l = v_l * t_l
    way_d = v_d * t_d
    return f"список: {way_l}/словарь {way_d}"


print(calculate_way(*data_list, **data_dict))
