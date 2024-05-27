# if 2 > 4:
#     print("This is the start of an execution block")  # line 2
#     print("This is part of the execution block")  # line 3
#     print("This is still part of the execution block")  # line 4
#     print("This is the end of an execution block")  # line 5
# print("It is not part of the execution block")  # line 6


# example_2
cycle_count = 0
while cycle_count < 5:
    print("Inside_cycle")
    cycle_count += 1

for i in range(5):
    print("Inside_cycle_range")

item_list = ["item_1", "item_2", "item_3", "item_4"]
for item in item_list:
    print(f"{item} inside cycle")

# # example_3
# try:
#     print("Example")
# except:
#     print("Some Exceptions")
# finally:
#     print("Handling Exceptions")


# example_4
def some_function():
    print("Inside_Function")


some_function()


class ExampleClass:

    def __init__(self, attr):
        self.attr = attr
        print("Inside __init__")

    def get_attr(self):
        print(self.attr)


example_1 = ExampleClass("Дмитрий")
example_1.get_attr()
