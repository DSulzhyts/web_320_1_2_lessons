def print_list_data(some_list):
    for element in some_list:
        print(element)


my_list = ["Новелла", "Роман", "Пьеса"]
print_list_data(my_list)


def dict_to_lists(some_dict):
    keys_list = []
    values_list = []
    for key, value in some_dict.items():
        keys_list.append(key)
        values_list.append(value)
    return keys_list, values_list


my_dict = {"cinema": "Боевик", "book": "Новелла"}

genres_keys, genres_values = dict_to_lists(my_dict)
print(genres_keys)
print(genres_values)

