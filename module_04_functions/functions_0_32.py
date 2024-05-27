def password_protected(password):
    def inner():
        if password == "secret":
            print("Доступ разрешен")
        else:
            print("В доступе отказано!")

    return inner


login = password_protected("secret")
print(password_protected)
print(login)
login()
print()
login_1 = password_protected("no_secret")
login_1()
