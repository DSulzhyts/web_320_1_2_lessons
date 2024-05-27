import re

# my_str = """Мои номера телефонов: А1 +375(029)6234567; МТС +375(033)3334455"""
# my_reg = r'Мои номера телефонов: А1 \+375\(029\)(\d\d\d\d\d\d\d); МТС \+375\(033\)(\d\d\d\d\d\d\d)'
#
# match_1 = re.match(my_reg, my_str)
# print(match_1.group(1))
# print(match_1.group(2))


string = """course topic part a"""
reg = r'course'

new_string = re.sub(reg, 'Module', string)
print(new_string)

string_2 = """course topic part a"""
reg_2 = r'topic'
string_split = re.split(reg_2, string_2)
print(string_split)
