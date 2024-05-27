import random

# active_days = [1, 5, 6, 8, 10, 12, 15, 19, 22, 27, 30]
#
# day = int(input("Введите число: "))
#
# if day in active_days:
#     print("Это был полезный день")
# else:
#     print("Это был бесполезный день")

# nums_list = []
# even_list = []
# odd_list = []
# positive_list = []
# negative_list = []
#
# for i in range(15):
#     nums_list.append(random.randint(-10, 10))
#
# for num in nums_list:
#     if num == 0:
#         continue
#
#     if num % 2 == 0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)
#
#     if num > 0:
#         positive_list.append(num)
#     else:
#         negative_list.append(num)
#
# print(even_list)
# print(odd_list)
# print(positive_list)
# print(negative_list)


my_str = input()
my_symbol = input()

print(my_str.count(my_symbol))
