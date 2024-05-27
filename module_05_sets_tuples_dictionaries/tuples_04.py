animals_tuple = 'Cat', 'Turtle', 'Snake', 'Dog'
print(animals_tuple)

cat, turtle, snake, dog = animals_tuple
print(cat, turtle, snake, dog)
print(*animals_tuple)

pet_1 = 'cat'
pet_2 = 'dog'

pet_1, pet_2 = pet_2, pet_1

print(f"Теперь pet_1 это {pet_1}")
print(f"Теперь pet_2 это {pet_2}")

a, b, c, d, e, f = [10, 20, 30, 40, 50, 60]
print(a)
