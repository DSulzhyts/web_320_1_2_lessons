cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]

print("Drama" in cinema_genres)
print("Detective" in cinema_genres)
print("Detective" not in cinema_genres)
print("Comedy" not in cinema_genres)


if "Drama" in cinema_genres:
    print("Drama есть в списке жанров!")
else:
    print("Такого жанра нет!")

if "Detective" not in cinema_genres:
    cinema_genres.append("Detective")
    print("Жанр добавлен")
else:
    print("Такой жанр уже есть!")


user_answer = input().lower()
if user_answer in ['да', 'yes', 'y']:
    pass