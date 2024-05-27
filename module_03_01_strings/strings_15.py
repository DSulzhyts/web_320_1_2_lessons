from string import Formatter, Template

formatter = Formatter()

print(formatter.format('{user_login}', user_login='Admin'))
print(formatter.format('{} {user_login}', 'Welcome', user_login='Admin'))

print(('{} {user_login}'.format('Welcome', user_login='Admin')))

my_template = Template('$user_login имеет права: $user_rights, в приложении: $app_name')

my_string_1 = my_template.substitute(user_login="Admin",
                                     user_rights="SuperUser",
                                     app_name="E-Shop")

my_string_2 = my_template.substitute(user_login="User",
                                     user_rights="read_only",
                                     app_name="E-Shop")

print(my_string_1)
print(my_string_2)

users_list = []
for i in range(5):
    user_login = input("Логин: ")
    user_rights = input("Права: ")
    user_app = input("Приложение: ")
    my_string = my_template.substitute(user_login=user_login,
                                       user_rights=user_rights,
                                       app_name=user_app)
    users_list.append(my_string)

for user_string in users_list:
    print(user_string)
