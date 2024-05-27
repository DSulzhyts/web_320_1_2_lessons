import os

path_module_06 = os.path.normpath(r'/module_06_00_files')
path_module_06_not_abs = os.path.normpath(r'.')

path_module_06_abs = os.path.abspath(r'm_06_01_02_paths.py')
print(path_module_06_abs)

print(os.path.isdir(path_module_06))
print(os.path.isdir(path_module_06_abs))
print(os.path.isfile(path_module_06_abs))

# new_dir = r'D:/work_Top_Academy_web/web_class_work/module_06_00_files/my_new_dir'
# os.rmdir(new_dir)


new_dir = os.path.normpath(r'my_new_dir_2\new_new')
os.rmdir(new_dir)