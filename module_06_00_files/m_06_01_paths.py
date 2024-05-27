import os

# path_module_06 = r'D:\work_Top_Academy_web\web_class_work\module_06_00_files\test_path_1'
#
# for path, dirnames, filenames in os.walk(path_module_06):
#     print(f"paths - {path}")
#     print(f"dirnames - {dirnames}")
#     print(f"filenames - {filenames}")


# path_module_06 = os.path.normpath(r'D:/work_Top_Academy_web/web_class_work/module_06_00_files')
#
# for path, dirnames, filenames in os.walk(path_module_06):
#     print(f"paths - {path}")
#     print(f"dirnames - {dirnames}")
#     print(f"filenames - {filenames}")

# disk = 'D:\\'
# dir_1 = 'work_Top_Academy_web'
# dir_2 = 'web_class_work'
# dir_3 = 'module_06_00_files'
# path_module_06 = os.path.join(disk, dir_1, dir_2, dir_3)
#
# print(path_module_06)
#
# for path, dirnames, filenames in os.walk(path_module_06):
#     print(f"paths - {path}")
#     print(f"dirnames - {dirnames}")
#     print(f"filenames - {filenames}")


base_dir = '.'
dir_1 = 'test_path_1'

path_module_06_ = os.path.join(base_dir, dir_1)
print(path_module_06_)

for path, dirnames, filenames in os.walk(path_module_06_):
    print(f"paths - {path}")
    print(f"dirnames - {dirnames}")
    print(f"filenames - {filenames}")