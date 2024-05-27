# my_dict = {"Cat": "Котейка"}
# my_dict["Dog"] = "Собачка"
#
# print(my_dict)
# my_dict["Cat"] = "Кошка"
# my_dict["Dog"] = "Собака"
# print(my_dict)
# del my_dict["Cat"]
# print(my_dict)


my_dict = {'Cat': 'Кошка', 'Dog': 'Собака'}
shop_dict = {'Parrot': 'Попугай', 'Snake': 'Змея'}
my_dict.update(shop_dict)
print(my_dict)