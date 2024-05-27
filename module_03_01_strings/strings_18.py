import re

my_str = "abcd abc egff"
my_reg = r'\w{4}'
match = re.search(my_reg, my_str)
print(match)

print(match.group())


my_str = "abcd abc 123 egff 456"
my_reg = r'\d{3}'
match = re.search(my_reg, my_str)
print(match)

print(match.group())
