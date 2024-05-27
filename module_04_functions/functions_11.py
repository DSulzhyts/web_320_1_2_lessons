def planet_space_address(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


planet_space_address(planet="Земля", star="Солнце", galaxy="Млечный Путь", age=round(4.543e9))
