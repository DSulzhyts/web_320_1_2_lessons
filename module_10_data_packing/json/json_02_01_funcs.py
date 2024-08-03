import json


class MyCat:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


my_cat = MyCat('Франц', 3, "самец")
json_data = json.dumps(my_cat.__dict__,
                       default=lambda obj_cat: obj_cat.__dict__,
                       ensure_ascii=False, indent=2)

print(json_data)

python_data = json.loads(json_data)
print(python_data)

with open('my_cat.json', 'w', encoding='utf-8') as fh:
    json.dump(my_cat, fh,
              default=lambda obj_cat: obj_cat.__dict__,
              ensure_ascii=False, indent=2)

with open('my_cat.json', 'r', encoding='utf-8') as fh:
    python_data_from_file = json.load(fh)

print(type(python_data_from_file))
