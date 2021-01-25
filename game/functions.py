import random
from .models import Enemy
from .data_struc import actions


def getMechByUser(MobileSuit, User, request):
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
        enemy = random.randint(1,Enemy.objects.count())
    else:
        enemy = None

    return {
        'text': action,
        'enemy': enemy,
    }