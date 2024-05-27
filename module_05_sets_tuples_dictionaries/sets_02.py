my_animals_set = {"Cat", "Dog", "Turtle", "Owl", "Snake"}
my_animals_set.add("Parrot")
print(my_animals_set)
# popped_animal = my_animals_set.pop()
# print(popped_animal)
# print(my_animals_set)

my_animals_set.discard("Turtle")
my_animals_set.discard("Turtle")
print(my_animals_set)

animal_to_remove = "Owl"
try:
    my_animals_set.remove("Owl")
except KeyError:
    print("Данный элемент отсутствует!")
else:
    print("Элемент успешно удален!")
finally:
    print("Программа завершила работу")


my_animals_set = {"Cat", "Dog", "Turtle", "Owl", "Snake"}
my_animals_set.clear()
print(my_animals_set)


my_animals_set = {"Cat", "Dog", "Turtle", "Owl", "Snake"}
for animal in my_animals_set:
    print(animal)


