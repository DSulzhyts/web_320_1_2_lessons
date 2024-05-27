from random import seed, randint

seed()
data = [randint(-10, 10) for x in range(10)]
filtered_data = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered_data)


def check(x):
    if x > 0 and x % 2 == 0:
        return True


data_1 = [randint(-10, 10) for i in range(10)]
print(data_1)
checked_data = list(filter(check, data_1))
print(checked_data)
