my_list = [10, 20, 30, 40, 50, 60]
my_tuple = (10, 20, 30, 40, 50, 60)
print(my_list.__sizeof__())
print(my_tuple.__sizeof__())

my_dict = {('a', 1): "value1", ('b', 2): "value2"}
print(my_dict[('a', 1)])
print(my_dict[('b', 2)])

mutable_tuple = ([1, 2, 3], [4, 5, 6])
print("Изменяемый кортеж", mutable_tuple)

mutable_tuple[0][1] = 10
mutable_tuple[1].append(7)

print(mutable_tuple)

