# file = open(r'test_path_1\test_1.txt', mode='rt')
# content = file.readlines()
# file.close()
# lines = []
#
# for line in content:
#     lines.append(line.strip())
#
# print(' '.join(lines))

my_filename = r'test_path_1\test_1.txt'


def get_file_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content_f = file.read()
    return content_f


print(get_file_data(my_filename))
