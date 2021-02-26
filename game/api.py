from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

from .models import MobileSuit, Enemy, Helm, Chest, LeftArm, RightArm, Legs, Modifier
from .functions import randomEvent, whoGoesFirst


### Deployment API ###

@login_required
def event(request):
    """Returns a JSON object containing a random patrol action"""
    if not request.session.get('deployed', False):
        return HttpResponseRedirect(reverse('deploy'))

    event = randomEvent()

    try:
        request.session['enemy'] = event.enemy.id
    except:
        pass


    data = {
        'event': event.serialize(),
        'buttons': event.getActions(),
    }

    return JsonResponse(data)


@login_required
def attack(request):
    """Initiate an attack round between mech and enemy"""
    if not request.session.get('deployed', False):
        return HttpResponseRedirect(reverse('deploy'))

    mech = MobileSuit.objects.filter(id=request.session['mech']).get()
    enemy = Enemy.objects.filter(id=request.session['enemy']).get()

    mech_health = '%s / %s' % (mech.current_hp, mech.max_hp)
    enemy_health = '%s / %s' % (enemy.current_hp, enemy.max_hp)

    first_player, second_player = whoGoesFirst(mech, enemy)
    request.session['first_player'] = first_player.id
    request.session['second_player'] = second_player.id

    data = {
        'mech': {
            'health': mech_health,
            'img': '/static/img/tinset/tinhelm.png',
        },
        'enemy': {
            'name': enemy.name,
            'img': enemy.img,
            'health': enemy_health,
        },
        'combat_order': {
            'firstPlayer': first_player.name,
            'secondPlayer': second_player.name,
        },
    }

    return JsonResponse(data)


@login_required
def fight(request):
    """Call a round of battle"""
    if not request.session.get('deployed', False):
        return HttpResponseRedirect(reverse('deploy'))

    if request.session.get('first_player') == request.session.get('mech'):
        first_player = MobileSuit.objects.filter(id=request.session.get('mech')).get()
        second_player = Enemy.objects.filter(id=request.session.get('enemy')).get()
    else:
        first_player = Enemy.objects.filter(id=request.session.get('enemy')).get()
        second_player = MobileSuit.objects.filter(id=request.session.get('mech')).get()

    data = {
        'move': 'You and the enemy flail at each other!',
        'first_player': first_player.name,
        'second_player': second_player.name,
    }

    return JsonResponse(data)


@login_required
def flee(request):
    """Defines a redirect for leaving the outlands"""
    request.session['deployed'] = False
    request.session['enemy'] = None
    
    return HttpResponseRedirect(reverse('workshop'))





### Equipment API ###

@login_required
def equipment(request, typ, pk):
    """Shows an individual piece of equipment"""
    request.session['deployed'] = False
    request.session['enemy'] = None

    types = {
        'helm': Helm,
        'chest': Chest,
        'leftarm': LeftArm,
        'rightarm': RightArm,
        'legs': Legs,
        'modifier': Modifier,
    }

    piece = types[typ].objects.filter(id=pk).get()
    
    data = piece.serialize()
    
    return JsonResponse(data)