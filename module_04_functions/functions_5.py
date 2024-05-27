from functions_4 import random_genre, random_genre_lists

user_choice = input("Чем вы хотите заняться кино/книги/игры: ")
print(random_genre(user_choice))

cinema = ["Драма", "Комедия", "Фэнтези", "Ужасы"]
book = ["Поэма", "Водевиль", "Роман", "Проза"]
games = ["Симулятор", "Аркада", "RPG", "Инди"]

user_choice_1 = input("Чем вы хотите заняться кино/книги/игры: ")
print(random_genre_lists())
