import random
from .models import Enemy, User, MobileSuit, EventBattle, EventDiscovery, EventNothing


def getMechByUser(request):
    """Returns the mobile suit of the logged in user"""
    return MobileSuit.objects.filter(
        controller=User.objects.filter(
        username=request.user.get_username()
        ).get()
        ).get()


def randomAction():
    """Returns a random action that occurs on patrol"""
    num = random.randint(1, 100)
    if num <= 60:
        event = random.choice(EventNothing.objects.all())
    elif num <= 70:
        event = random.choice(EventDiscovery.objects.all())
    else:
        event = EventBattle(
            name='You encounter an enemy!',
            desc='You may choose to engage the enemy or run away',
            enemy=random.choice(Enemy.objects.all())
            )

    action = event

    return action



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
