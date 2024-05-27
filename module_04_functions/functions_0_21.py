# my_list_comprehension = [1 if num_c % 2 == 0 else 0 for num_c in range(10)]
# my_generator = (1 if num_c % 2 == 0 else 0 for num_c in range(10))

for value in [1 if num_c % 2 == 0 else 0 for num_c in range(10)]:
    print(value, end=' ')
print()


for value in (1 if num_c % 2 == 0 else 0 for num_c in range(10)):
    print(value, end=' ')
print()

