# def push(val):
#     stack.append(val)
#
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val


# def push(stack, val):
#     stack.append(val)
#
#
# def pop(stack):
#     if stack:
#         val = stack.pop()
#     else:
#         return "Stack is empty!"
#     return val
#
#
# my_stack = []
# push(my_stack, 3)
# push(my_stack, 2)
# push(my_stack, 1)
# print(pop(my_stack))
# print(pop(my_stack))
# print(pop(my_stack))
# print(pop(my_stack))


def push(stack, val):
    stack.append(val)


def pop(stack):
    try:
        val = stack.pop()
    except IndexError:
        return "Stack is empty!"
    else:
        return val


my_stack = []
push(my_stack, 3)
push(my_stack, 2)
push(my_stack, 1)
print(pop(my_stack))
print(pop(my_stack))
print(pop(my_stack))
print(pop(my_stack))
