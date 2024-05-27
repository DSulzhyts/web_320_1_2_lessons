def degrees_of_2(n):
    degree = 1
    for i in range(n):
        yield degree
        degree *= 2


for y in range(20):
    if y in degrees_of_2(5):
        print(y)