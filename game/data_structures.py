import random

actions = {
        'battle': {
            'text': 'An enemy is sighted!',
            'enemy': 1,
        },
        'nothing': {
            'text': 'Nothing happens...',
            'enemy': None,
        },
        'cave': {
            'text': 'You discover a cave!',
            'enemy': None,
        },
    }


actionz = [
    'Nothing',
    'Battle',
    'Discovery',
]

def spam():
    action = random.choice(actionz)
    if action == 'Battle':
        enemy = random.randint(1,3)
    else:
        enemy = None

    return {
        'text': action,
        'enemy': enemy,
    }