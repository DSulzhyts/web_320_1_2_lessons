import re

users_list = []
users_names = ["Иван", "Иван", "Николай", "Егор"]
users_surnames = ["Петров", "Петров", "Сидоров", "Иванов"]
users_phones = ["+375(17)1111111", "+375(17)1111111", "+375(17)3333333", "+375(17)4444444"]
check_phones_set = set()
users_mails = ["mail@yandex.ru", "mail@yandex.ru", "mail_2@yandex.ru", "mail_3@yandex.ru"]
check_emails_set = set()

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
            if bool(reg_name.match(user_name)) is True:
                user_data_list.append(user_name)
                print("Имя принято!")
            else:
                print("Ввод некорректен\nПовторите ввод!")
                continue
        if len(user_data_list) < 2:
            # user_surname = input("Введите фамилию пользователя: ")
            user_surname = users_surnames[counter]
            if bool(reg_surname.match(user_surname)) is True:
                user_data_list.append(user_surname)
                print("Фамилия принята!")
            else:
                print("Ввод некорректен\nПовторите ввод!")
                continue

        if len(user_data_list) < 3:
            user_phone = users_phones[counter]
            if reg_phone.match(user_phone):
                if len(users_list) > 0:
                    for user in users_list:
                        check_phones_set.add(user[2])
                if user_phone in check_phones_set:
                    print("Такой телефон уже есть!")
                    user_data_list.clear()
                    counter += 1
                    continue
                user_data_list.append(user_phone)
                print("Телефон принят!")
            else:
                print("Ввод некорректен\nПовторите ввод!")
                continue

        if len(user_data_list) < 4:
            # user_mail = input("Введите email пользователя на yandex.ru: ")
            user_mail = users_mails[counter]
            if reg_email.match(user_mail):
                if len(users_list) > 0:
                    for user in users_list:
                        check_emails_set.add(user[3])
                if user_mail in check_emails_set:
                    print("Такая почта уже есть!")
                    user_data_list.clear()
                    counter += 1
                    continue
                user_data_list.append(user_mail)
                print("email принят!")
            else:
                print("Ввод некорректен\nПовторите ввод!")
                continue
    counter += 1
    users_list.append(user_data_list)

print()
[print(user) for user in users_list]
