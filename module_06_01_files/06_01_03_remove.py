
import shutil

try:
    shutil.rmtree('test_path_1')
except FileNotFoundError:
    print("Директория не найдена!")
else:
    print("Удалена директория со всем содержимым!")

