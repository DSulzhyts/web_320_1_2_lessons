cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres = cinema_genres
some_list = ["item_1", "item_2", "item_3"]

print(f"Кино {cinema_genres}")
print(f"Литература {literature_genres}")

literature_genres.append("Scy-Fy")

print(f"Литература {literature_genres}")
print(f"Кино {cinema_genres}")

print(literature_genres is cinema_genres)
print(cinema_genres is literature_genres)
print(literature_genres is some_list)
print(cinema_genres is some_list)