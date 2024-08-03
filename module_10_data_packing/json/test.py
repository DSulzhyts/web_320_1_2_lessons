import json


class MyPlane:

    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    @staticmethod
    def to_json(obj):
        if isinstance(obj, MyPlane):
            result = obj.__dict__
            result['ClassName'] = obj.__class__.__name__
            result['Methods'] = ['Many Nethods']
            return result


my_plane = MyPlane("Ту-134", 12, "10 лет")

json_data = json.dumps(my_plane, default=MyPlane.to_json, ensure_ascii=False, indent=2)
with open('my_cat_func.json', 'w', encoding='utf-8') as fh:
    json.dump(my_plane, fh, default=MyPlane.to_json, ensure_ascii=False, indent=2)

print(json_data)
