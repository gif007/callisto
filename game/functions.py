import random
from .models import Enemy, User, MobileSuit
from .data_struc import actions


def getMechByUser(request):
    """Returns the mobile suit of the logged in user"""
    return MobileSuit.objects.filter(
        controller=User.objects.filter(
        username=request.user.get_username()
        ).get()
        ).get()


def randomAction():
    """Returns a random action that occurs on patrol"""
    action = random.choice(actions)

    if action == 'Battle':
        enemy = Enemy.objects.filter(
        id=random.randint(1,Enemy.objects.count())
        ).get()
    else:
        enemy = None

    return {
        'text': action,
        'enemy': enemy,
    }



from .models import MobileSuit

def get_stats(id):
    """Intended to be used within a shell session to quickly get stats on a suit"""
    suit = MobileSuit.objects.filter(id=id).get()
    print('Name: %s' % suit.name)
    print('Health: %s/%s' % (suit.current_hp, suit.max_hp))
    print('Controller: %s' % suit.controller)
    print('Firepower: %s' % suit.get_firepower_value())
    print('Armor: %s' % suit.get_armor_value())
    print('Speed: %s' % suit.get_speed_value())
    print('Vision: %s' % suit.get_sight_value())
