import os

# base_path = r'test_path_1\test_1.txt'
# new_path = r'test_path_2\test_1.txt'


base_path = r'test_path_2\test_1.txt'
new_path = r'test_path_1\test_new_name.txt'

try:
    os.rename(base_path, new_path)
except FileNotFoundError:
    print("Файл не найден")

base_path_1 = r'test_path_2\test_renames.txt'
base_path_2 = r'test_path_2\shopping_renames.txt'

new_path_1 = r'test_path_1\test_renames.txt'
new_path_2 = r'test_path_1\shopping_renames.txt'

try:
    os.renames(base_path_1, new_path_1)
    os.renames(base_path_2, new_path_2)
except FileNotFoundError:
    print("Файл не найден")


