# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# exampleObject = ExampleClass(1)
#
# try:
#     print(exampleObject.a)
# except AttributeError:
#     print("Атрибут exampleObject.a не существует")
#
# try:
#     print(exampleObject.b)
# except AttributeError:
#     print("Атрибут exampleObject.b не существует")


# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = "есть"
#
#
# exampleObject = ExampleClass(2)
#
# if hasattr(exampleObject, 'a'):
#     print(exampleObject.a)
# if hasattr(exampleObject, 'b'):
#     print(exampleObject.b)


# class ExampleClass:
#     attr = 1
#
#
# print(hasattr(ExampleClass, 'attr'))
# print(hasattr(ExampleClass, 'attr_1'))


# class ExampleClass:
#     attr_1 = 1
#
#
#
# if ExampleClass.attr_1:
#     print(ExampleClass.attr_1)
# if ExampleClass.attr_2:
#     print(ExampleClass.attr_2)
#
#     # print(hasattr(ExampleClass, 'attr'))
#     # print(hasattr(ExampleClass, 'attr+1'))


# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = "есть"
#
#
# exampleObject = ExampleClass(2)
# if 'a' in ExampleClass:
#     print(exampleObject.a)
# if 'b' in ExampleClass:
#     print(exampleObject.b)

class ExampleClass:
    a = 1

    def __init__(self, b=2):
        self.b = b


example_object = ExampleClass()

print(hasattr(example_object, 'a'))
print(hasattr(example_object, 'b'))
print(hasattr(ExampleClass, 'a'))
print(hasattr(ExampleClass, 'b'))
