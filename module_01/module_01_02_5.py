# num_str = "123"
# if "." in num_str:
#     print("Это float")
# else:
#     num_int = int(num_str)
#     print(type(num_int))
#
# num_2_str = "123.15"
# num_2_float = float(num_2_str)
# print(type(num_2_float))

# print("Как вас зовут?")
# user_name = input()
# print(f"Привет {user_name}!")
#
# print("Введите 2 числа для расчета баланса")
# user_num_1 = int(input())
# user_num_2 = input()
# user_num_2_int = int(user_num_2)
# print(f"Баланс {user_num_2_int - user_num_1}!")

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число:\n"))

number_3 = (number_2 * number_1 * number_1 * number_1 * number_1 * number_1
            * number_1 * number_1 * number_1 * number_1 * number_1)
print(number_3)