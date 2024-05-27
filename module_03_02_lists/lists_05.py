# example_list_str = ["Drama", "Comedy", "Fantasy"]
# print(example_list_str)
#
# example_list_str[0] = "Драма"
# example_list_str[1] = "Комедия"
# example_list_str[2] = "Фэнтези"
#
# print(example_list_str)

example_list_str = ["Drama", "Comedy", "Zantasy", "Алфавит"]
example_list_nums = [3, 1, 2, 11]

print(len(example_list_str), len(example_list_nums))
print(max(example_list_str), max(example_list_nums))
print(min(example_list_str), min(example_list_nums))
print(sum(example_list_nums))

sorted_list = sorted(example_list_str)
sorted_nums = sorted(example_list_nums)
print(sorted_list)
print(sorted_nums)

sorted_lis_rev = sorted(example_list_str, reverse=True)
sorted_nums_rev = sorted(example_list_nums, reverse=True)
print(sorted_lis_rev)
print(sorted_nums_rev)

example_list_nums = ["03", "01", "02", "11"]
sorted_nums_rev = sorted(example_list_nums, reverse=True)
print(sorted_nums_rev)