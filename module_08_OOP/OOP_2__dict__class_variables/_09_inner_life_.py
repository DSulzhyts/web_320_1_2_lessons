# class MyClass:
#     pass
#
#
# obj = MyClass()
# obj.a = 1
# obj.b = 2
# obj.i = 3
# obj.ireal = 3.5
# obj.integer = 4
# obj.z = 5
#
#
# def inc_ints_i(obj):
#     for name in obj.__dict__.keys():
#         if name.startswith('i'):
#             val = getattr(obj, name)
#             if isinstance(val, int):
#                 setattr(obj, name, val + 1)
#
#
# print(obj.__dict__)
# inc_ints_i(obj)
# print(obj.__dict__)


class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 2


def inc_ints_i(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)
