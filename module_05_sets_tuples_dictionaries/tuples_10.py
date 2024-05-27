# animals_tuple = ('Cat', 'Turtle', 'Snake', 'Dog')
# animals_list = list(animals_tuple)
# animals_list[2] = "Python"
# animals_list.append('Owl')
# animals_list.remove('Turtle')
# animals_tuple = tuple(animals_list)
# print(animals_tuple)

animals_tuple = ('Cat', 'Turtle', 'Snake', 'Dog')
updated_tuple = animals_tuple[:2] + ('Python',) + animals_tuple[3:] + ('Owl',)
print(animals_tuple)
print(updated_tuple)