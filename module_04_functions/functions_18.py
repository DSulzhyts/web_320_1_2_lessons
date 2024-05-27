str_counter = 0


def print_number_of_str_elements():
    global str_counter
    elements = ["Новелла", "Роман", "Пьеса"]
    for element in elements:
        if type(element) is str:
            str_counter += 1
    print(f"Количество строк в списке {str_counter}")


print_number_of_str_elements()
print(f"Счетчик строк: {str_counter}")
print()
print_number_of_str_elements()
print(f"Счетчик строк: {str_counter}")
