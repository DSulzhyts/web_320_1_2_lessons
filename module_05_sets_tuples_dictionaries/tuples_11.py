animals_tuple = ('CatDog', 'Turtle', 'Snake', 'DogCat')
print(animals_tuple.count('Cat'))

animal_to_search = 'Cat'
counter = 0
for animal in animals_tuple:
    if animal_to_search in animal:
        counter += 1

print(counter)
