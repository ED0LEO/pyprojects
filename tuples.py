def match_food_lists(fav_food_list, names_list):
    #traversing lists simultaneously
    for f, n in zip(fav_food_list, names_list):
        print("Food = ", f, ", Person = ", n)

def print_indexes(names_list):
    #indexing names
    for i, name in enumerate(names_list):
        print("Index = ",i, ", Name = ", name)


def match_food_dict(dic):
    #print from dictionary
    for food, name in dic.items():
        print("Food = ", food, ", Person = ", name)


fav_food_list = ["Milk", "Strawberries", "Cheese", "Soup", "Candy"]
names_list = ["Clara", "Don", "Jake", "Bob", "Alice"]

d = dict(zip(fav_food_list, names_list))

print("Match food from lists:\n")
match_food_lists(fav_food_list, names_list)

print("\nPrint indexes:\n")
print_indexes(names_list)

print("\nMatch food from dict:\n")
match_food_dict(d)
