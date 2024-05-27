def new_summ(*args):
    print(args)
    sum_ = 0
    for num in args:
        sum_ += num
    return sum_


print(new_summ(1, 5, 6, 7, 8, 9, 10, 11, 12))



