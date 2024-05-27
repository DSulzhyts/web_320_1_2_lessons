cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres = cinema_genres.copy()

print(literature_genres is cinema_genres)
print(cinema_genres is literature_genres)

literature_genres.append("Poem")

print(f"Литература {literature_genres}")
print(f"Кино {cinema_genres}")

cinema_genres_1 = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres_1 = list(cinema_genres)

print(literature_genres_1 is cinema_genres_1)
print(cinema_genres_1 is literature_genres_1)

literature_genres_1.append("Poem")

print(f"Литература {literature_genres_1}")
print(f"Кино {cinema_genres_1}")


cinema_genres_2 = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres_2 = cinema_genres_2[:]

print(literature_genres_2 is cinema_genres_2)
print(cinema_genres_2 is literature_genres_2)

literature_genres_2.append("Poem")

print(f"Литература {literature_genres_2}")
print(f"Кино {cinema_genres_2}")


cinema_genres_3 = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres_3 = ["Drama", "Comedy", "Fantasy", "Romance"]

for i in range(len(cinema_genres_2)):
    literature_genres_3.append(cinema_genres_3[i])

print(literature_genres_3 is cinema_genres_3)
print(cinema_genres_3 is literature_genres_3)

print(literature_genres_3)


cinema_genres_3 = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres_3 = ["Drama", "Comedy", "Fantasy", "Romance", "Romance"]

literature_genres_3 = cinema_genres_3.copy()
print(literature_genres_3)