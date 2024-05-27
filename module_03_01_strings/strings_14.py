import string
import random

# user_login = "".join(random.sample(string.ascii_lowercase, 20))
# print(user_login)
# user_pass = "".join(random.sample((string.ascii_letters + string.digits), 8))
# print(user_pass)

# print(string.ascii_lowercase)
#
# symbols_list = []
# for i in range(500):
#     symbols_list.append(random.choice(string.ascii_lowercase))
#
# print("".join(symbols_list))

my_string = " Мы рады\n встречать\n\n старых друзей.  "
print(my_string)
print(string.capwords(my_string))

new_string = string.capwords(my_string)
print(string.capwords(new_string, sep='а'))
print(string.capwords(my_string, sep='а'))


