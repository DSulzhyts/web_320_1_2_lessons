# managers_dict = {}
#
# with open('managers_data.txt', encoding='utf-8') as managers_data:
#     for manager_data in managers_data:
#         clean_data = manager_data.strip().split(':')
#         manager = clean_data[0]
#         company = clean_data[1]
#         boss_company = clean_data[2]
#         managers_dict[(company, boss_company)] = manager
#
# print(managers_dict)
#
# for companies, manager in managers_dict.items():
#     print(f"{manager} работает в компании {companies[0]} которая принадлежит {companies[1]}")

managers_for_write = {('Bethesda', 'Microsoft'): 'Тодд Говард',
                      ('ID Software', 'Microsoft'): 'Джон Кармак',
                      ('AMD', 'AMD'): 'Лиза Су'}

with open('managers_data_writed.txt', 'w', encoding='utf-8') as managers_data:
    for companies, manager in managers_for_write.items():
        managers_data.write(f"{manager}||{companies[0]}||{companies[1]}\n")
print("Я вирус")
