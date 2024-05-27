import random

# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# print(cinema_genres)
# random.shuffle(cinema_genres)
#
# print(cinema_genres)
#
#
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Horror"]
# genres_sample = random.sample(cinema_genres, 3)
# print(genres_sample)
#
#
# some_str = "Привет! Я строка!"
# items = (random.sample(some_str, len(some_str)))
# print(items)
# result = ''.join(items)
# print(result)


cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Horror"]
# random_genre = random.choice(cinema_genres)
# print(random_genre)

for i in range(len(cinema_genres)):
    random_genre = random.choice(cinema_genres)
    print(random_genre)
    cinema_genres.remove(random_genre)

print(cinema_genres)
