def calc(numbers: list):
    summ = 0
    for number in numbers:
        summ += int(number)
    return summ


def main():
    user_numbers = input("Введите числа через пробел: ")
    numbers_list = user_numbers.split(" ")
    result = calc(numbers_list)
    print(result)


main()
