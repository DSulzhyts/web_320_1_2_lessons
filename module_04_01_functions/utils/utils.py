import random


def random_genre_print():
    cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Horror"]
    genre = random.sample(cinema_genres, 1)[0]
    print(f"Сегодня смотрим {genre}")


def random_genre_return():
    random_genres = []
    cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Horror"]
    for genre in cinema_genres:
        random_genres.append(genre[:4])
    return random_genres, cinema_genres


