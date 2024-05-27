# with open('write_data.txt', 'wt', encoding='utf-8') as file:
#     file.write("Hello World!\n")
#     file.write("Hello Python!\n")
#     file.write("Hello Dmitriy!\n")


# with open('write_data.txt', 'at', encoding='utf-8') as file:
#     file.write("Hello World!\n")
#     file.write("Hello Python!\n")
#     file.write("Hello Dmitriy!\n")


user_language = input("Какой язык вы изучаете: ")
user_time = input("Как давно? ")
user_institution = input("Где? ")

user_answers = [user_language, user_time, user_institution]

with open('user_answers.txt', 'w', encoding='utf-8') as file:
    for answer in user_answers:
        file.write(f"{answer}\n")

print("Ответы записаны!")

