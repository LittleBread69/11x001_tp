##NOT IN CLASS
from pprint import pprint

##CLASS
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Munich"],
}

pprint(travel_log)
print(travel_log["France"][1])


travel_log_2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
    "number_of_times_visited": 8
    },
    "Germany": {
        "cities_visited": ["Berlin", "Munich"],
        "number_of_times_visited": 3,
        },
}

pprint(travel_log_2)
print(travel_log_2["France"]["cities_visited"][1])
print(travel_log_2.keys())
print(list(travel_log_2.keys()))

# lists
liste_2 = ["Apples", "Oranges", "Pears",]
index = liste_2.index("Oranges")
