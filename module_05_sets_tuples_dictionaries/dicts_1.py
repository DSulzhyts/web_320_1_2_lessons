my_dict = {}

my_dict_1 = {"Петр": 1234567, "Мария": 1234567}
my_dict_2 = {"Петр": "Имя", "Python": "Язык программирования"}
my_dict_num = {1: "Имя", 2: "Язык программирования"}

my_dict_3 = dict(Петр="Имя", Python="Язык программирования")
print(my_dict_3)

print(my_dict_2["Петр"])
print(my_dict_num[2])

explanations = {True: "Да все верно", False: "Это не верно!"}

if 3 < 2:
    print(explanations[True])
else:
    print(explanations[False])

print(explanations[3 > 2])
print(explanations[3 < 2])
