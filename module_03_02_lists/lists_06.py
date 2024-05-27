# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
#
# for cinema_genre in cinema_genres:
#     print(cinema_genre)
#
# for index in range(len(cinema_genres)):
#     print(f"{index+1} {cinema_genres[index]}")
#
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# cinema_genres.append("Action")
# print(cinema_genres)
#
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# cinema_genres.extend(["Action", "Detective"])
# print(cinema_genres)
#
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# genres_to_add = ["Action", "Detective"]
# cinema_genres.extend(genres_to_add)
# print(cinema_genres)
#
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# cinema_genres.insert(1, "Action")
# print(cinema_genres)
#
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
# for cinema_genre in cinema_genres:
#     if cinema_genre == "Comedy":
#         cinema_genres.remove("Comedy")
#
# print(cinema_genres)
#
#
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# deleted_genre = cinema_genres.pop()
# print(cinema_genres)
# print(deleted_genre)
#
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# cinema_genres.clear()
# print(cinema_genres)
#
#
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# print(cinema_genres.index("Fantasy"))


cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
cinema_genres.sort()
print(cinema_genres)
cinema_genres.sort(reverse=True)
print(cinema_genres)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
cinema_genres.reverse()
print(cinema_genres)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
example_list_nums = [3, 1, 2, 11, 2.5, 3.5]
cinema_genres.extend(example_list_nums)
print(cinema_genres)

example_list_nums.sort()
print(example_list_nums)

