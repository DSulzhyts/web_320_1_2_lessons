# start = 0
# end = 0
# num_1 = int(input("Введите начало: "))
# num_2 = int(input("Введите конец: "))
#
# if num_1 > num_2:
#     start = num_2
#     end = num_1
# else:
#     start = num_1
#     end = num_2
#
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         print(i)


# num_1 = int(input("Введите начало: "))
# num_2 = int(input("Введите конец: "))
# nums_list = [num_1, num_2]
#
# for i in range(min(nums_list), max(nums_list) + 1):
#     if i % 2 != 0:
#         print(i)

# num = int(input("Введите длину линии *"))
# line = ""
# for i in range(num):
#     line += "*"
#
# print(line)


# num = int(input("Введите длину линии: "))
# line = ""
# symbol = input("Введите символ для заполнения: ")
# for i in range(num):
#     line += symbol
#
# print(line)

# import random
#
# random_number = random.randint(1, 500)
# print(random_number)
# counter = 1
#
# user_number = int(input("Введите число: "))
#
# for i in range(501):
#     if user_number == 0:
#         counter -= 1
#         break
#     elif user_number == random_number:
#         break
#     elif user_number < random_number:
#         print("Загаданное число больше")
#     else:
#         print("Загаданное число меньше")
#     counter += 1
#     user_number = int(input("Введите число!"))
#
# print(f"Всего попыток {counter}")


num_1 = int(input("Введите начало диапазона: "))
num_2 = int(input("Введите конец диапазона: "))
num_3 = int(input("Введите число в диапазоне: "))

# while True:
#     if num_1 <= num_3 <= num_2:
#         break
#     else:
#         num_3 = int(input(f"Неверно! Введите число в диапазоне от {num_1} до {num_2} включительно!: "))

while num_3 < num_1 or num_3 > num_2:
    num_3 = int(input(f"Неверно! Введите число в диапазоне от {num_1} до {num_2} включительно!: "))

for i in range(num_1, num_2 + 1):
    if i == num_3:
        print(f"!{i}!")
    else:
        print(i)
