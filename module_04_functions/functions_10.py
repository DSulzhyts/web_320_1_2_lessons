def get_personal_data(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['surname'])
    print(kwargs['age'])
    print(kwargs['phone'])


get_personal_data(name="Василий", surname="Рогов", age=35, phone=102)
