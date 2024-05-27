from random import random, seed

# 0.0 <= x < 1

for i in range(5):
    print(random())

print()
seed(0)

for i in range(5):
    print(random())