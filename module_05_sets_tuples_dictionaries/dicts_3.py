my_dict = {'Cat': 'Кошка', 'Dog': 'Собака'}

print(my_dict['Cat'])
my_dict["die Katze"] = my_dict['Cat']
print(my_dict)
del my_dict['Cat']
print(my_dict)

popped_data = my_dict.pop('Dog')
print(popped_data)
print(my_dict)
# my_dict['der Hund'] = my_dict.pop('Dog')
# print(my_dict)

