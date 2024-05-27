my_list = [2 ** i for i in range(10)]
print(my_list)

my_list_1 = []
for i in range(10):
    my_list_1.append(2 ** i)
print(my_list_1)

my_list = [i * i for i in range(11)]
print(my_list)

square_list = []
for i in range(11):
    square_list.append(i * i)
print(square_list)

list_from_str = [sym + "*" for sym in "my_string"]
print(list_from_str)

list_from_str_1 = []
for sym in "my_string":
    list_from_str_1.append(sym + "*")
print(list_from_str_1)


list_from_str_1 = [sym * 5 for sym in "my_string"]
print(list_from_str_1)

list_from_str_2 = []
for sym in "my_string":
    list_from_str_2.append(sym * 5)
print(list_from_str_2)
