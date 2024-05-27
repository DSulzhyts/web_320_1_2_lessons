def get_numbers_digits(some_tuple):
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    for num in some_tuple:
        if len(str(num)) == 1:
            counter_1 += 1
        elif len(str(num)) == 2:
            counter_2 += 1
        elif len(str(num)) == 3:
            counter_3 += 1
    return counter_1, counter_2, counter_3


my_nums_tuple = (1, 2, 3, 22, 33, 44, 55, 123, 231)

digit_1, digit_2, digit_3 = get_numbers_digits(my_nums_tuple)
print(f"Одна цифра - {digit_1} элемента")
print(f"Две цифры - {digit_2} элемента")
print(f"Три цифры - {digit_3} элемента")

