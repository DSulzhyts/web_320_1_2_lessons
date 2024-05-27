def get_number_of_str_elements():
    str_counter = 0
    elements = ["Новелла", 1, "Роман", 2, "Пьеса"]

    def count_number_of_elements():
        nonlocal str_counter

        for element in elements:
            if type(element) is str:
                str_counter += 1

        return str_counter

    return count_number_of_elements


number_of_elements = get_number_of_str_elements()
print(number_of_elements())
