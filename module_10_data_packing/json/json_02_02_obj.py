import json


class MyCat:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def to_json(obj):
        if isinstance(obj, MyCat):
            result = obj.__dict__
            result['ClassName'] = obj.__class__.__name__
            result['Methods'] = ["Many Methods"]
            return result


my_cat = MyCat('Франц', 3, "самец")
json_data = json.dumps(my_cat,
                       default=MyCat.to_json,
                       ensure_ascii=False, indent=2)

with open('my_cat_func.json', 'w', encoding='utf-8') as fh:
    json.dump(my_cat, fh,
              default=MyCat.to_json,
              ensure_ascii=False, indent=2)

with open('my_cat_func.json', 'r', encoding='utf-8') as fh:
    python_data_from_file = json.load(fh)

print(json_data)
python_data = json.loads(json_data)
print(python_data)
print(python_data_from_file)
