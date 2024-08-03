class SuperOne:
    pass


class SuperMixin:
    pass


class Sub(SuperMixin, SuperOne):
    pass


def print_bases(cls):
    print('(', end=' ')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


print_bases(SuperOne)
print_bases(SuperMixin)
print_bases(Sub)
