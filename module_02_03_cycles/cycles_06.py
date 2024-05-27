# str_data = "привет я строка!"
# str_data_up = str_data.upper()
# print(str_data_up)
#
#
# str_data = "ПРИВЕТ Я СТРОКА!"
# str_data_low = str_data.lower()
# print(str_data_low)
#
#
# str_data = "привет я строка! Привет я строка!"
# str_data_cap = str_data.capitalize()
# print(str_data_cap)
#
#
# str_data = "привет я строка! Привет я строка!"
# str_data_title = str_data.title()
# print(str_data_title)


# str_data = "    привет я строка!    "
# print(str_data.strip())
# print(str_data.rstrip())
# print(str_data.lstrip())


# str_data = "    ПРИВЕТ Я СТРОКА!    "
# print(str_data.lower().strip())
# print(str_data.rstrip().title())
# print(str_data.capitalize().lstrip())
# print(str_data.lower().strip().replace("привет", "пока"))
# print(str_data.replace("ПРИВЕТ", "пока").lower().strip())

# str_list = ["один\n", "два\n", "три\n"]
# str_list_1 = []
#
# for item in str_list:
#     new_item = item.strip()
#     str_list_1.append(new_item)
#
# str_1 = " ".join(str_list_1)
# print(str_1)

# str_list = ["один\n", "два\n", "три\n"]
#
# for i in range(len(str_list)):
#     str_list[i] = str_list[i].strip()
#
# str_2 = " ".join(str_list)
# print(str_2)
#
#
# str_list = ['111\n', '222\n', '333\n']
# x = ''
# for item in str_list:
#     x += item.replace('\n', ' ')
#
# print(x)
