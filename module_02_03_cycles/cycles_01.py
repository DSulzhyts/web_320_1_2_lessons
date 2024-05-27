odd_numbers = 0
even_numbers = 0

number = int(input("Введите число или напишите 0 чтобы остановить программу: "))

while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Введите число или напишите 0 чтобы остановить программу: "))

print(f"Количество нечетных чисел {odd_numbers}")
print(f"Количество четных чисел {even_numbers}")
