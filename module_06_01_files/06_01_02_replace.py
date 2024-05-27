import os
base_path = r'test_2.txt'
new_path = r'test_path_1\test_2.txt'

try:
    os.replace(base_path, new_path)
except FileNotFoundError:
    print("Файл не найден")