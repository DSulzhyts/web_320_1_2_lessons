# my_string = "Hello World!"
# string_slice = my_string[0:5]
# print(string_slice)
#
# string_slice_1 = my_string[:5]
# print(string_slice_1)
#
# string_slice_2 = my_string[6:11]
# print(string_slice_2)
#
# string_slice_3 = my_string[6:]
# print(string_slice_3)
#
# my_string = "Hello World!"
# string_slice_4 = my_string[-6:]
# print(string_slice_4)
#
# string_slice_4 = my_string[:-7]
# print(string_slice_4)
#
# string_slice_5 = my_string[-6:-3]
# print(string_slice_5)
#
# string_slice_6 = my_string[-6:11]
# print(string_slice_6)

my_string = "Hello World!"
string_slice_step = my_string[6:11:2]
print(string_slice_step)

string_slice_step_1 = my_string[3::2]
print(string_slice_step_1)

string_slice_step_2 = my_string[:8:2]
print(string_slice_step_2)

string_slice_step_3 = my_string[::2]
print(string_slice_step_3)

string_slice_step_4 = my_string[::-1]
print(string_slice_step_4)

string_slice_step_5 = my_string[::-2]
print(string_slice_step_5)
