fruits = {
    "яблоки": 100,
    "груши": 200,
    "персики": 400,
    "мандарины": 300,
    "апельсины": 350
}

for key, value in fruits.items():
    fruits[key] = round(value * 1.1)

print(fruits)
