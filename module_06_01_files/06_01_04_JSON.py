
import os

file_path = 'json_data/levels.json'

print(os.path.getctime(file_path))
print(os.path.getmtime(file_path))
print(os.path.getatime(file_path))
print(os.path.getsize(file_path))


