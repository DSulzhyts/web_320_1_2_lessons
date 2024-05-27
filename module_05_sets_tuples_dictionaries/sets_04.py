# my_animals = {"Cat", "Dog"}
# shop_animals = {"Cat", "Turtle", "Snake"}
# wild_animals = {"Fox", "Owl", "Snake"}
#
# all_animals = my_animals.union(shop_animals).union(wild_animals)
# print(all_animals)
#
# same_animals = my_animals.intersection(shop_animals)
# print(same_animals)
#
# only_my_animals = my_animals.difference(shop_animals)
# print(only_my_animals)
#
# only_shop_animals = shop_animals.difference(my_animals)
# print(only_shop_animals)

my_animals = {"Cat", "Dog"}
shop_animals = {"Cat", "Turtle", "Snake", "Dog"}

result = my_animals.issubset(shop_animals)
print(result)

my_anymals = {'Cat', 'Parrot', 'Owl'}
shop_anymals = {'Turtle', 'Parrot', 'Rat'}
shelter_anymals = {'Dog', 'Cat'}
# 1
im_shop = shop_anymals.difference(my_anymals)
print(im_shop)
# 2
in_shelter = shelter_anymals.intersection(my_anymals)
print(in_shelter)
# 3
not_shelter_not_shope1 = my_anymals.difference(shop_anymals)
not_shelter_not_shope2 = not_shelter_not_shope1.difference(shelter_anymals)
print(not_shelter_not_shope2)

# 4

in_my = shelter_anymals.union(my_anymals)
in_my_all = shop_anymals.union(in_my)
print(in_my_all)

shop_animals = {"Cat", "Turtle", "Snake", "Parrot"}
wild_animals = {"Fox", "Owl", "Snake", "Turtle"}

shop_animals.update(wild_animals)
print(shop_animals)

shop_animals = {"Cat", "Turtle", "Snake", "Parrot"}
wild_animals = {"Fox", "Owl", "Snake", "Turtle"}

shop_animals.intersection_update(wild_animals)
print(shop_animals)

shop_animals = {"Cat", "Turtle", "Snake", "Parrot"}
wild_animals = {"Fox", "Owl", "Snake", "Turtle"}

shop_animals.difference_update(wild_animals)
print(shop_animals)

shop_animals = {"Cat", "Turtle", "Snake", "Parrot"}
wild_animals = {"Fox", "Owl", "Snake", "Turtle"}

shop_animals.symmetric_difference_update(wild_animals)
print(shop_animals)

