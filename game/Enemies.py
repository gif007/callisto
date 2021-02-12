"""This file contains a bunch of dictionaries that provide properties for enemies"""

# The following is an example of an enemy template
# wolf = {
#     'name': 'Wolf',
#     'desc': 'A common lupin',
#     'max_hp': 50,
#     'current_hp': 50,
#     'firepower': 5,
#     'armor': 5
# }

gelatinous_blob = {
    'name': 'Gelatinous Blob',
    'desc': 'A slimey creature with no fixed shape',
    'max_hp': 150,
    'current_hp': 150,
    'firepower': 2,
    'firerate': 0.5,
    'armor': 5,
}

ice_spider = {
    'name': 'Ice Spider',
    'desc': 'An arachnid-like organism that is completely incased in ice',
    'max_hp': 75,
    'current_hp': 75,
    'firepower': 5,
    'firerate': 1.7,
    'armor': 30,
}

rock_spider = {
    'name': 'Rock Spider',
    'desc': 'An arachnid-like organism that is completely made of rock',
    'max_hp': 75,
    'current_hp': 75,
    'firepower': 5,
    'firerate': 2.2,
    'armor': 20,
}

eel = {
    'name': 'Eel',
    'desc': 'A saltwater eel from the oceanic depths below the surface',
    'max_hp': 100,
    'current_hp': 100,
    'firepower': 15,
    'firerate': 1,
    'armor': 10,
}

ENEMIES = [
    gelatinous_blob,
    ice_spider,
    rock_spider,
    eel,

]