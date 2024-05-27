# num = float(input('Введите число: '))
# deg = int(input('В какую степень в диапазоне 0-7 возвести число: '))
#
# while deg not in [0, 1, 2, 3, 4, 5, 6, 7]:
#     print("Ввели не верные данные")
#     deg = int(input('В какую степень в диапазоне 0-7 возвести число: '))
#
# print("Результат:", num ** deg)

# tariffs = {
#     ('мтс', 'мтс'): 50,
#     ('мтс', 'билайн'): 100,
#     ('мтс', 'мегафон'): 150,
#     ('билайн', 'мтс'): 90,
#     ('билайн', 'билайн'): 60,
#     ('билайн', 'мегафон'): 140,
#     ('мегафон', 'мтс'): 180,
#     ('мегафон', 'билайн'): 200,
#     ('мегафон', 'мегафон'): 30
# }
#
# time = int(input("Введите время звонка: "))
# operator_a = input("Выберете оператора с которого мы звоним: ").lower()
# operator_b = input("Выберете оператора на который мы звоним: ").lower()
#
# if (operator_a, operator_b) not in tariffs.keys():
#     print("Ошибка, не знаю таких операторов!")
# else:
#     cost = time * tariffs[(operator_a, operator_b)]
#     print(f"Стоимость разговора составляет: {cost} рублей.")


man1 = int(input(f'Продажи Игнатия: '))
man2 = int(input(f'Продажи Евпатия: '))
man3 = int(input(f'Продажи Евлампия: '))

sales_man_list = [man1, man2, man3]
zp_list = []
salary = 200

for sales_man in sales_man_list:
    salary_man = 0
    if sales_man < 500:
        salary_man = salary * 1.03
    elif 500 <= sales_man <= 1000:
        salary_man = salary * 1.05
    else:
        salary_man = salary * 1.08
    zp_list.append(salary_man)

print(f'Зарплата Игнатия {zp_list[0]}$.\nЗарплата Евпатия {zp_list[1]}$.\nЗарплата Евлампия {zp_list[2]}$.')

if max(zp_list) == zp_list[0]:
    print(f"Лучший менеджер Игнатий он получает {zp_list[0] + 200}$")
elif max(zp_list) == zp_list[1]:
    print(f"Лучший менеджер Евпатий он получает {zp_list[1] + 200}$")
else:
    print(f"Лучший менеджер Евлампий он получает {zp_list[2] + 200}$")


