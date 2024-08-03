# class Classy:
#
#     def __init__(self, first=1):
#         self.first = first
#
#
# print(Classy.__name__)
# obj = Classy()
# print(type(obj))
# print(type(obj).__name__)


class Classy:

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    print(Classy.__module__)
    obj = Classy('ClassyObj')
    print(obj.__module__)
