# string_alnum = "abc123"
# print(string_alnum.isalnum())
#
# string_alnum = "123"
# print(string_alnum.isalnum())
#
# string_alnum = "abc123"
# print(string_alnum.isalnum())
#
# string_alpha = "abc"
# print(string_alpha.isalpha())
#
# string_alpha = "abc123"
# print(string_alpha.isalpha())
#
# string_digit = "123"
# print(string_digit.isdigit())
#
# string_space = "    "
# print(string_space.isspace())
# string_space_1 = "   \n\t abc "
# print(string_space_1.isspace())


# string_lower = "hello python13!"
# print(string_lower.islower())
#
# string_lower = "HELLO PYTHON13!"
# print(string_lower.isupper())
#
# string_lower = "Hello Python13!"
# print(string_lower.istitle())

string_alnum = "abc123"
print(string_alnum.isalnum())

import re


user_password = input("Введите желаемый пароль: ")
reg = re.compile('''^[!@#$%^&*(){} \\[\\]/~.,_:;<>\\-="'?№]+$''')

if user_password.isalnum() is True:
    print("Пароль должен содержать спецсимволы")
elif bool(reg.match(user_password)):
    print("Пароль не может содержать только спецсимволы")
else:
    print("Ваш пароль принят!")
