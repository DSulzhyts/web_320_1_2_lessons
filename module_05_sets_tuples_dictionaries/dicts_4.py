# my_dict = {'Cat': 'Кошка', 'Dog': 'Собака'}
#
# word = 'Cat'
# if word in my_dict:
#     print(my_dict[word])
# else:
#     print("Не знаю таких слов!")
#
#
# try:
#     print(my_dict[word])
# except KeyError:
#     print(f"Такого ключа {word} нет в словаре")
# finally:
#     print("Программа завершила свою работу!")


my_dict = {'Cat': 'Кошка', 'Dog': 'Собака'}
get_animal = my_dict.get('Cat')
print(get_animal)
get_animal_1 = my_dict.get('Bird')
print(get_animal_1)

get_animal_2 = my_dict.setdefault('Dog')
my_dict['Dog'] = "Собака"
print(get_animal_2)
get_animal_3 = my_dict.setdefault('Bird')
print(my_dict)

my_dict['Bird'] = "Птица"
print(my_dict)



