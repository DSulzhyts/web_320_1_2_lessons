a = 3

print("Global a = ", a)


def fun():
    a = 4
    print("Local a = ", a)


fun()

print("Global a = ", a)


a = 30

print("Global a = ", a)


def fun():
    print("Local a = ", a)


fun()

print("Global a = ", a)

