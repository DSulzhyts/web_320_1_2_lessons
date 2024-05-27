# def greet(greeting, name):
#     print(f"{greeting}, {name}!")
#
#
# greet("Привет", "Дмитрий")


def greet_curried(greeting):
    def greet(name):
        print(f"{greeting}, {name}!")

    return greet


greet_hello = greet_curried("Привет")
print(greet_hello)
greet_hello("Дмитрий")
greet_hello("Иван")

