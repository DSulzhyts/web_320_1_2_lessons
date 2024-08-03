# class ExampleClass:
#     def __init__(self, first=1, second=2):
#         self.first = first
#         self.second = second
#
#     def set_second(self, second):
#         self.second = second
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5
#
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)
#     def __init__(self, first=1, second=2):
#         self.first = first
#         self.second = second
#
#     def set_second(self, second):
#         self.second = second
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5
#
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)


class ExampleClass:
    counter = 0

    def __init__(self, first=1):
        self.first = first
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
