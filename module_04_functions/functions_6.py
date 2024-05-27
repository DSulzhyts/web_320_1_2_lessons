# def check(prices, tip=0):
#     sum_ = sum(prices)
#     total = sum_ * (100 + tip) / 100
#     return total
#
#
# check_sum = [1000, 3000, 4000]
#
# print(check(check_sum))
# print(check(check_sum, 10))


def paint_total(width, height, consumption=0.2, layers=2):
    total = width * height * consumption * layers
    return round(total, 2)


print("Итого литров", paint_total(3, 4))
print("Итого литров", paint_total(3, 4, 0.4))
print("Итого литров", paint_total(3, 4, 0.2, 3))
