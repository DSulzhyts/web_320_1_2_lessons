from math import e, exp, log

print(pow(e, 1))
print(pow(e, 1) == exp(log(e)))

print(pow(4, 2))
print(pow(2, 2) == exp(2 * log(2)))

print(log(e, e))
print(log(e, e) == exp(0))
