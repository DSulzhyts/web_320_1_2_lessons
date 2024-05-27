import re

my_str = """Мои номера телефонов: А1 +375(029)6234567; МТС +375(033)3334455"""
my_reg = r'А1 \+375\(029\)(\d\d\d\d\d\d\d); МТС \+375\(033\)(\d\d\d\d\d\d\d)'
match = re.search(my_reg, my_str)
# print(match.group())
# print(match.group(1))
# print(match.group(2))

my_str = """Мои номера телефонов: А1 +375(029)6234567; МТС +375(033)3334455"""
my_reg = r'(А1) \+375\(029\)(\d{7}); (МТС) \+375\(033\)(\d{7})'
match = re.search(my_reg, my_str)
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))
# print(match.group(3))
# print(match.group(4))
#
# print(match.group(1, 2, 3, 4))
# print(type(match.group(1, 2, 3, 4)))

print(match.start(), match.end())
print(match.start(1), match.end(1))
print(match.start(2), match.end(2))
print(match.start(3), match.end(3))
print(match.start(4), match.end(4))

print(match.span())
print(match.span(1))
print(match.span(2))
print(match.span(3))
print(match.span(4))

start, end = (match.span())
print(start, end)