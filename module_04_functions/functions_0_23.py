four = lambda: 4
sqr = lambda x: x * x
deg = lambda x, y: x ** y

# print(four())
# print(sqr(3))
# print(deg(2, 8))

for a in range(-2, 3):
    print(f"Квадрат {sqr(a)}", end="/")
    print(f"Степень {deg(a, four())}")
