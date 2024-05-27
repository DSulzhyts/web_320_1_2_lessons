import string
import re

user_password = input("Введите желаемый пароль: ")
# reg = re.compile('''^[!@#$%^&*(){} \\[\\]/~.,_:;<>\\-="'?№]+$''')
reg = re.compile('[' + string.punctuation + ']' + '+')

if user_password.isalnum() is True:
    print("Пароль должен содержать спецсимволы")
elif bool(reg.match(user_password)):
    print("Пароль не может содержать только спецсимволы или начинаться с них")
else:
    print("Ваш пароль принят!")
