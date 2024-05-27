import re

reg_name = re.compile(r'^[A-Za-zА-Яа-я]+$')
reg_surname = re.compile(r'^[A-Za-zА-Яа-я]+$')
reg_phone = re.compile(r'[+]\d{1,3}\(\d{1,3}\)(\d{7})$')
reg_email = re.compile(r'[A-Za-z0-9_]+@yandex\.ru$')

user_name = input("Введите имя пользователя: ")

if bool(reg_name.match(user_name)) is True:
    print("Имя принято!")
else:
    print("Ввод некорректен\nПовторите ввод!")

user_surname = input("Введите фамилию пользователя: ")

if bool(reg_surname.match(user_surname)) is True:
    print("Фамилия принята!")
else:
    print("Ввод некорректен\nПовторите ввод!")

user_phone = input("Введите номер телефона: ")
if reg_phone.match(user_phone):
    print("Телефон принят!")
else:
    print("Ввод некорректен\nПовторите ввод!")

user_mail = input("Введите email пользователя на yandex.ru: ")
if reg_email.match(user_mail):
    print("email принят!")
else:
    print("Ввод некорректен\nПовторите ввод!")
