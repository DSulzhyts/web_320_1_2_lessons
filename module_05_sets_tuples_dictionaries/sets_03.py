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
