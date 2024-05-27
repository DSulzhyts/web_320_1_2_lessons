import re


def get_reg_data():
    """Функция возвращает паттерны регулярных выражений"""
    reg_name = re.compile(r'^[A-Za-zА-Яа-я]+$')
    reg_surname = re.compile(r'^[A-Za-zА-Яа-я]+$')
    reg_phone = re.compile(r'[+]\d{1,3}\(\d{1,3}\)(\d{7})$')
    reg_email = re.compile(r'[A-Za-z0-9_]+@yandex\.ru$')
    reg_patterns_list = [reg_name, reg_surname, reg_phone, reg_email]
    return reg_patterns_list


def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    """Функция принимает данные от пользователя проверяет их по заданному паттерну
    проверяет на уникальность введенных данных (только телефон и email)
    и если все проверки пройдены, возвращает проверенные введенные данные"""
    while True:
        if reg_pattern.match(user_data):
            if len(users_list) > 0 and data_to_check:
                if not check_unique_data(user_data, data_to_check):
                    user_data = input()
                    continue

        else:
            print("Ввод некорректен\nПовторите ввод!")
            user_data = input()
            continue
        print(f"{user_data} - данные приняты!")
        return user_data


def check_unique_data(user_data, data_to_check):
    """Функция служит для проверки уникальности телефона и email"""
    if user_data in data_to_check:
        print("Такие данные уже есть".center(30, "!"))
        print("Введите уникальные данные!")
        return False
    else:
        return True









