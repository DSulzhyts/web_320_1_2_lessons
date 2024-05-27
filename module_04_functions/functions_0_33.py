def make_closer(par):
    loc = par

    def power(par_2):
        return par_2 ** loc

    return power

par = 2
f_square = make_closer(par)
par = 3
f_cube = make_closer(par)

for par_2 in range(5):
    print(par_2, f_square(par_2), f_cube(par_2))

