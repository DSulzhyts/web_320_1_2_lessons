def degrees_of_2(n):
    degree = 1
    for i in range(n):
        yield degree
        degree *= 2


values = [value for value in degrees_of_2(5)]
print(values)

values_list = list(degrees_of_2(5))
print(values_list)