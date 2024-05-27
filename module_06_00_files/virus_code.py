virus_code = 'print("Я вирус")'

with open('m_06_04_own_data_1.py', 'a', encoding='utf-8') as file:
    file.write(f"\n{virus_code}\n")

code_to_remove = 'print("Я вирус")'

with open('m_06_04_own_data_1.py', encoding='utf-8') as file:
    content = file.read()

    if code_to_remove in content:
        print("Вирус обнаружен!")
        clean_content = content.replace('print("Я вирус")', '')
        with open('m_06_04_own_data_1.py', 'w', encoding='utf-8') as clean_file:
            clean_file.write(clean_content)
    else:
        print("Вирусов нет!")
