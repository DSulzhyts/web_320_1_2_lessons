import json


class MyCat:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_data(self):
        return self.name, self.age, self.gender


class MyCatEncoder(json.JSONEncoder):

    def default(self, o):
        return {
            "Name": o.name,
            "Age": o.age,
            "Gender": o.gender,
            "Methods": {
                "get_data": o.get_data()
            },
            "ClassName": o.__class__.__name__
        }


my_cat = MyCat('Франц', 3, "самец")
json_data = json.dumps(my_cat, cls=MyCatEncoder, ensure_ascii=False, indent=4)
print(json_data)

python_data = json.loads(json_data)
print(python_data)

with open('my_cat_encode.json', 'w', encoding='utf-8') as fh:
    json.dump(my_cat, fh, cls=MyCatEncoder, ensure_ascii=False)

with open('my_cat_encode.json', encoding='utf-8') as fh:
    python_data_from_file = json.load(fh)
print(python_data_from_file)