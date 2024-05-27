def my_space_address_mix(name: str, age=35, city=None, *args, **kwargs):
    print(name)
    print(age)
    if city:
        print(city)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key, value)


my_space_address_mix("Дмитрий", 36, "Минск", "Беларусь", "Восточная Европа", planet="Земля", star="Солнце")
