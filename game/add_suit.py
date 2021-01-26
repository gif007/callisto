from game.models import MobileSuit
"""
This file was written to test out how easy it would be to create models programatically
instead of using the admin site. It could be faster to implement with CSV
"""
suit_params = {
    'name': 'George',
    'max_hp': 1000,
    'current_hp': 500,
}

suit = MobileSuit(**suit_params)
suit.save()