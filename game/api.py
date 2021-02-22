from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

from .models import MobileSuit, Enemy, Helm, Chest, LeftArm, RightArm, Legs, Modifier
from .functions import randomEvent


### Deployment API ###

@login_required
def get_action(request, action=randomEvent):
    """Returns a JSON object containing a random patrol action"""
    if not request.session.get('deployed', False):
        return HttpResponseRedirect(reverse('deploy'))

    event = action()

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
    mech = MobileSuit.objects.filter(id=request.session['mech']).get()
    enemy = Enemy.objects.filter(id=request.session['enemy']).get()

    mech_health = '%s/%s' % (mech.current_hp, mech.max_hp)
    enemy_health = '%s/%s' % (enemy.current_hp, enemy.max_hp)

    data = {
        'mech_health': mech_health,
        'enemy_health': enemy_health,
        'enemy': enemy.name
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