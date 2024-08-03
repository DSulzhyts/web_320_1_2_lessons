
import pickle

my_data = {
    'nums': [1, 2.0, 3, 4 + 6],
    'strings': ("character_string", b"byte_string"),
    'other': {None, True, False}
}

# для обычной работы
my_data_s = pickle.dumps(my_data, pickle.HIGHEST_PROTOCOL)
print(my_data_s)
my_data_ds = pickle.loads(my_data_s)
print(my_data_ds)

# для записи в файл
with open('data_pickle.pkl', 'wb') as file:
    pickle.dump(my_data_ds, file, protocol=5)

# для чтения из файла
with open('data_pickle.pkl', 'rb') as file:
    my_data_ff = pickle.load(file)

print(my_data_ff)
