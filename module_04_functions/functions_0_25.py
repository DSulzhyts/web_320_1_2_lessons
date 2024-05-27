def printfunction(args, fun):
    for x in args:
        print(f'f({x}) = {fun(x)}', sep=', ')

                                             # return
printfunction([-2, -1, 0, 1, 2, 3, 5], lambda x: 2 * x ** 2 - 4 * x + 2)
