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
    'max_hp': 100,
    'current_hp': 100,
    'firepower': 2,
    'firerate': 0.5
    'armor': 15
}

ENEMIES = [
    gelatinous_blob,
]