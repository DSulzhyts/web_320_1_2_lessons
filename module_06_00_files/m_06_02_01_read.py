file = open(r'test_path_1\test_1.txt', mode='rt')
conter = 0
for line in file:
    print(line.strip())
    conter += 1
file.close()
print(conter)

with open(r'test_path_1\test_1.txt', mode='rt') as file:
    for line in file:
        print(line.strip())


file = open(r'test_path_1\test_1.txt', mode='rt')
conter = 0
for line in file:
    print(line, end='')
    conter += 1
file.close()



