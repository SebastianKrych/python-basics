# In Python, we create sets by placing all the elements inside curly braces {},
# separated by comma.
#
# A set can have any number of items, and they may be of different types
# (integer, float, tuple, string etc.).
# But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

empty_set = set()

brands = {"Mazda", "Ford", "BMW"}

brands.add("Opel")

for brand in brands:
    print(brand)

#add two sets
german_brands = {"Audi", "BMW"}
american_brands = {"Chevrolte", "Buick"}

all_brands = german_brands.union(american_brands)
print(all_brands)
