my_animals_frozenset = frozenset({"Cat", "Dog", "Turtle", "Owl", "Snake"})
wild_animals_frozenset = ("Wolf", "Owl", "Snake", "Fox", "Bear")
subset = {'Cat', 'Dog'}
no_subset = {"Wolf", "Fox", "Bear"}

all_animals_frozenset = my_animals_frozenset.union(wild_animals_frozenset)
print(all_animals_frozenset)
print(my_animals_frozenset.difference(wild_animals_frozenset))
print(my_animals_frozenset.intersection(wild_animals_frozenset))
print(subset.issubset(my_animals_frozenset))
print(my_animals_frozenset.issuperset(subset))
print(my_animals_frozenset.isdisjoint(no_subset))
print(my_animals_frozenset.symmetric_difference(wild_animals_frozenset))
