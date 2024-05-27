my_list_comprehension = [1 if num_c % 2 == 0 else 0 for num_c in range(10)]
my_generator = (1 if num_c % 2 == 0 else 0 for num_c in range(10))
my_generator = (1 if num_c % 2 == 0 else 0 for num_c in range(5))

for value in my_list_comprehension:
    print(value, end=' ')
print()

print(my_generator)
my_list = [my_generator]

print(my_list)
for value in my_generator:
    print(value, end=' ')
print()

print(type(my_list_comprehension))
print(type(my_generator))
