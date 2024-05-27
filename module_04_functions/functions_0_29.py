from functools import reduce

my_nums_list = [i + 1 for i in range(5)]
print(my_nums_list)

reduce_summ = reduce(lambda num1, num2: num1 + num2, my_nums_list)
print(reduce_summ)

reduce_product = reduce(lambda num1, num2: num1 * num2, my_nums_list)
print(reduce_product)
