import random


def random_genre(category):
    cinema_genres = ["Драма", "Комедия", "Фэнтези", "Ужасы"]
    book_genres = ["Поэма", "Водевиль", "Роман", "Проза"]
    game_genres = ["Симулятор", "Аркада", "RPG", "Инди"]

    if category == "кино":
        return random.choice(cinema_genres)

    elif category == "книги":
        return random.choice(book_genres)

    elif category == "игры":
        return random.choice(game_genres)

    else:
        return "Не знаю такой категории!"


def random_genre_lists(category: str, cinema_genres: list, book_genres: list, game_genres: list):
    if category == "кино":
        return random.choice(cinema_genres)

    elif category == "книги":
        return random.choice(book_genres)

    elif category == "игры":
        return random.choice(game_genres)

    else:
        return "Не знаю такой категории!"
