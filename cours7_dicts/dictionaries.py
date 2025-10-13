#NOT PART OF CLASS
from __future__ import annotations

#PART OF CLASS
programming_dict = {
    "Bug": "An Error",
    "Function": "A code I can call",
}

print(programming_dict)

# Lists: recall getting an item at a position
liste = ["a", "b", "c"]
print(liste[0])

# Dictionaries: use the key to get an item
print(programming_dict["Bug"])

# New entry in dictionnary
programming_dict["Loop"] = "Action of doing something over and over again"

print(programming_dict)

# Empty dictionnary
emptry_dict = {}
print(emptry_dict)

# Change the dict value
programming_dict["Bug"] = "An insect"
print(programming_dict)

# Empty a dictionnary
programming_dict = {}
print(programming_dict)


programming_dict = {
    "Bug": "An Error",
    "Function": "A code I can call",
}

#Loop through a dict
for thing in programming_dict:
    print(thing)
    print(programming_dict[thing])

#Loop through dict items
for k, v in programming_dict.items():
    print(k, v, sep=": ")
