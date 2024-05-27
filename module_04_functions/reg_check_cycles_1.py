import re


def reg_check(user_data, reg_pattern, data_to_check=None):
    global users_list
    global user_data_list
    if reg_pattern.match(user_data):
        if len(users_list) > 0 and data_to_check:
            if not check_unique_data(user_data, data_to_check):
                return False
        user_data_list.append(user_data)
        print(f"{user_data} - данные приняты")
        return True
    else:
        print("Ввод некорректен\nПовторите ввод!")
        return False


def check_unique_data(user_data, data_to_check):
    global user_data_list
    global counter
    if user_data in data_to_check:
        print("Такие данные уже есть".center(30, "!"))
        print()
        user_data_list.clear()
        counter += 1
        return False
    else:
        return True


users_list = []
users_names = ["Иван", "Иван", "Николай", "Егор"]
users_surnames = ["Петров", "Петров", "Сидоров", "Иванов"]
users_phones = ["+375(17)1111111", "+375(17)1111111", "+375(17)3333333", "+375(17)4444444"]
check_phones_list = []

users_mails = ["mail@yandex.ru", "mail@yandex.ru", "mail_2@yandex.ru", "mail_3@yandex.ru"]
check_emails_list = []

reg_name = re.compile(r'^[A-Za-zА-Яа-я]+$')
reg_surname = re.compile(r'^[A-Za-zА-Яа-я]+$')
reg_phone = re.compile(r'[+]\d{1,3}\(\d{1,3}\)(\d{7})$')
reg_email = re.compile(r'[A-Za-z0-9_]+@yandex\.ru$')

counter = 0

while len(users_list) < 3:
    user_data_list = []
    while len(user_data_list) < 4:
        if len(user_data_list) < 1:
            # user_name = input("Введите имя пользователя: ")
            user_name = users_names[counter]
            if reg_check(user_name, reg_name):
                pass
            else:
                continue
        if len(user_data_list) < 2:
            # user_surname = input("Введите фамилию пользователя: ")
            user_surname = users_surnames[counter]
            if reg_check(user_surname, reg_name):
                pass
            else:
                continue

        if len(user_data_list) < 3:
            user_phone = users_phones[counter]
            if reg_check(user_phone, reg_phone, check_phones_list):
                pass
            else:
                continue

        if len(user_data_list) < 4:
            # user_mail = input("Введите email пользователя на yandex.ru: ")
            user_mail = users_mails[counter]
            if reg_check(user_mail, reg_email, check_emails_list):
                pass
            else:
                continue

    counter += 1
    users_list.append(user_data_list)
    check_phones_list.append(user_data_list[2])
    check_emails_list.append(user_data_list[3])
    print()

print()
[print(user) for user in users_list]
