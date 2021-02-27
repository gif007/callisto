"""This file contains a bunch of dictionaries that provide properties for enemies"""



gelatinous_blob = {
    'name': 'Gelatinous Blob',
    'prefix': 'a',
    'desc': 'A slimey creature with no fixed shape',
    'max_hp': 50,
    'current_hp': 50,
    'firepower': 6,
    'firerate': 0.5,
    'armor': 5,
    'speed': 1,
    'img': '/static/img/gelatinousblob.jpg',
}

ice_spider = {
    'name': 'Ice Spider',
    'prefix': 'an',
    'desc': 'An arachnid-like organism that is completely incased in ice',
    'max_hp': 75,
    'current_hp': 75,
    'firepower': 5,
    'firerate': 1.7,
    'armor': 30,
    'speed': 1,
    'img': '/static/img/icespider.jpg',
}

rock_spider = {
    'name': 'Rock Spider',
    'prefix': 'a',
    'desc': 'An arachnid-like organism that is completely made of rock',
    'max_hp': 75,
    'current_hp': 75,
    'firepower': 5,
    'firerate': 2.2,
    'armor': 20,
    'speed': 1,
    'img': '/static/img/rockspider.jpg',
}

eel = {
    'name': 'Eel',
    'prefix': 'an',
    'desc': 'A saltwater eel from the oceanic depths below the surface',
    'max_hp': 40,
    'current_hp': 40,
    'firepower': 15,
    'firerate': 1,
    'armor': 10,
    'speed': 1,
    'img': '/static/img/eel.jpg',
}

ENEMIES = [
    gelatinous_blob,
    ice_spider,
    rock_spider,
    eel,

]