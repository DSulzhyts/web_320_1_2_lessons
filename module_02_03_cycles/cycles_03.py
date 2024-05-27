# piggy_bank = 0
# user_sum = int(input("Сколько копим"))
#
# while piggy_bank < user_sum:
#     deposit = int(input("Введите сумму пополнения: "))
#     piggy_bank += deposit
#     print(f"Сумма {piggy_bank}")
#
# print(f"Цель достигнута удалось накопить {piggy_bank}")


# bank_summ = 10_000
# goal_summ = 20_000
# counter = 0
#
# while bank_summ < goal_summ:
#     bank_summ += bank_summ * 0.1 / 12
#     counter += 1
#
# print(counter)

# months = 18 * 12
# print(months)


# account = 0
# months = 0
#
# while account < 10000:
#     deposit = int(input("Введите сумму пополнения: "))
#     account += deposit
#     months += 1
#
# print(months)

# distance = 2
# day = 1
# while distance <= 5:
#     distance += distance * 0.2
#     day += 1
# print(f'Количество дней {day}')


# user_total = 0
# user_exp = input("Введите сумму расхода: ")
#
# while user_exp != "стоп":
#     user_total += int(user_exp)
#     user_exp = input("Введите сумму расхода: ")
#
# print(user_total)
#

# user_total = 0
#
# while True:
#     user_exp = input("Введите сумму расхода: ")
#     if user_exp == "стоп" or user_exp = "stop":
#         break
#     else:
#         user_total += int(user_exp)
#
# print(user_total)


shopping_list = []

while True:
    user_sum = input('Введите покупку: ')
    if user_sum == 'стоп':
        break
    shopping_list.append(user_sum)

for item in shopping_list:
    print(item)

[print(item) for item in shopping_list]
