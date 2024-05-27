# my_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица'}
#
# my_dict_keys = my_dict.keys()
# my_dict_values = my_dict.values()
#
# print(my_dict_keys)
# print(my_dict_values)
# print(type(list(my_dict_keys)))
# print(type(list(my_dict_values)))


# my_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица'}
# for key in my_dict:
#     print(key)
#     print(my_dict[key])
#
# keys_list = [key for key in my_dict]
# values_list = [my_dict[key] for key in my_dict]
# print(keys_list)
# print(values_list)


# my_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица'}
#
# for key in my_dict.keys():
#     print(key)
#
# for value in my_dict.values():
#     print(value)


my_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица'}
dict_keys = []
dict_values = []

for key, value in my_dict.items():
    dict_keys.append(key)
    dict_values.append(value)

print(dict_keys)
print(dict_values)

