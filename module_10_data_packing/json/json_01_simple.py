import json

my_dict = {
    "my_string": "some_string",
    "my_integer": 123,
    "my_tuple": (1, 2, 3, 4, 5),
    "my_bool": True,
    "my_none": None
}

with open('my_data.json', 'w', encoding='utf-8') as fh:
    json.dump(my_dict, fh, ensure_ascii=False, indent=1)
    # my_json = json.dumps(my_dict, ensure_ascii=False, indent=1)
    # fh.write(my_json)

with open('my_data_1.json') as fh:
    python_data = json.load(fh)
    # json_data = fh.read()
    # python_data = json.loads(json_data)

print(python_data)

# my_json = json.dumps(my_dict)
# print(my_json)
# print(type(my_json))
#
# my_dict = json.loads(my_json)
# print(my_dict)
# print(type(my_dict))
#
# for key, value in my_dict.items():
#     if 'tuple' in key:
#         my_dict[key] = tuple(value)
#
# print(my_dict)
