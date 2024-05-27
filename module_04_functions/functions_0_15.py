def func(n):
    for i in range(n):
        return i


print(func(10))


def func(n):
    for i in range(n):
        yield i


for value in func(10):
    print(value)


def degrees_of_2(n):
    degree = 1
    for i in range(n):
        yield degree
        degree *= 2


[print(value) for value in degrees_of_2(10)]
