def fibs_gen(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            p, pp = pp, n
            yield n


fibs_list = list(fibs_gen(10))
print(fibs_list)
