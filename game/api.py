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
def engage(request):
    """Initiate an attack round between mech and enemy"""
    if not request.session.get('deployed', False):
        return HttpResponseRedirect(reverse('workshop'))

    mech = MobileSuit.objects.filter(id=request.session['mech']).get()
    enemy = Enemy.objects.filter(id=request.session['enemy']).get()

    curr, _next = whoGoesFirst(mech, enemy)

    request.session['current_player'] = curr.id
    request.session['next_player'] = _next.id
    
    data = {
        'mech': {
            'health': mech.get_health(),
            'img': '/static/img/tinset/tinhelm.png',
        },
        'enemy': {
            'name': enemy.name,
            'img': enemy.img,
            'health': enemy.get_health(),
        },
        'currentPlayer': {
            'name': curr.name,
            'isMech': True if curr == mech else False,
        },
    }

    return JsonResponse(data)


@login_required
def attack(request):
    """Call a round of battle"""
    if not request.session.get('deployed', False):
        return HttpResponseRedirect(reverse('workshop'))

    try:
        enemy = Enemy.objects.filter(id=request.session.get('enemy')).get()
    except:
        data = {
            'dead': 'he dead',
        }
        return JsonResponse(data)

    mech = MobileSuit.objects.filter(id=request.session.get('mech')).get()

    if request.session['current_player'] == mech.id:
        curr, _next = mech, enemy
    else:
        curr, _next = enemy, mech

    _next_health = curr.attack(_next)

    if _next_health <= 0: # Wrap into attack()
        return _next.die()

    attacker = curr
    curr, _next = _next, curr

    request.session['current_player'] = curr.id # try putting this on one line
    request.session['next_player'] = _next.id

    data = {
        'mech_health': mech.get_health(),
        'enemy_health': enemy.get_health(),
        'isMech': True if attacker == mech else False,
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


@login_required
def heal(request):
    """Top up mech health"""
    request.session['deployed'] = False
    request.session['enemy'] = None

    mech = MobileSuit.objects.filter(id=request.session['mech']).get()
    mech.current_hp = mech.max_hp
    mech.save()

    data = {
        'mech_health': mech.current_hp,
    }

    return JsonResponse(data)