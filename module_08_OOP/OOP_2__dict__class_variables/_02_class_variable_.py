# class ExampleClass:
#     __counter = 0
#
#     def __init__(self, first=1):
#         self.first = first
#         ExampleClass.__counter += 1
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)
#
# print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
# print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
# print(example_object_3.__dict__, example_object_3._ExampleClass__counter)

class ExampleClass:
    variable = 1

    def __init__(self, value):
        ExampleClass.variable = value


print(ExampleClass.__dict__)
exampleObject = ExampleClass(2)

print(ExampleClass.__dict__)
print(exampleObject.__dict__)
