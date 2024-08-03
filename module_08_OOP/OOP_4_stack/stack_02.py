class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        try:
            val = self.__stack_list.pop()
        except IndexError:
            return "Stack is empty!"
        else:
            return val


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def get_sum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val

class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        super().push(val)

    def pop(self):
        val = super().pop()
        self.__sum -= val
        return val


stack_object = AddingStack()
for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())
for i in range(5):
    print(stack_object.pop())
