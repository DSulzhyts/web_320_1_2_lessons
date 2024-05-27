# my_string = "Hello World!"
# center_string = my_string.center(20)
# print(center_string)
#
# center_string = my_string.center(20, "*")
# print(center_string)
#
# center_string = my_string.center(3, "*")
# print(center_string)


# my_string = "Hello World!"
# left_string = my_string.ljust(20)
# left_string_1 = my_string.ljust(20, "/")
# print(left_string)
# print(left_string_1)
#
# my_string = "Hello World!"
# right_string = my_string.rjust(20)
# right_string_1 = my_string.rjust(20, "/")
# print(right_string)
# print(right_string_1)

# my_string = "Hello World!\n\t\tHello Pyhon!"
# print(my_string)
# my_string_expand = my_string.expandtabs()
# print(my_string_expand)
# my_string_expand = my_string.expandtabs(tabsize=12)
# print(my_string_expand)

# my_string = "***Hello World! Hello Pyhon!***"
# new_string = my_string.strip('*')
# print(new_string)


# with open('strip_file.txt', 'r', encoding='utf-8') as file:
#     file_data = file.readlines()
#     for line in range(len(file_data)):
#         file_data[line] = file_data[line].replace("\n", "")
#
#     print(" ".join(file_data))

# my_nums_string = "12345"
# print(my_nums_string.zfill(10))
#
# my_nums_string = "abcd"
# print(my_nums_string.zfill(10))


my_nums_string = "+12345"
print(my_nums_string.zfill(10))

my_nums_string = "-12345"
print(my_nums_string.zfill(10))

my_nums_string = "*12345"
print(my_nums_string.zfill(10))
my_nums_string = "/12345"
print(my_nums_string.zfill(10))

tel_code = "+375"
print(tel_code.zfill(5))
