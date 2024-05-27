def outer(par):
    loc = par

    def inner():
        return loc

    return inner


var = 1
result = outer(var)
print(result())