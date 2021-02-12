from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

from .models import MobileSuit, Enemy, Helm, Chest, LeftArm, RightArm, Legs, Modifier
from .functions import randomAction


@login_required
def get_action(request, action=randomAction):
    """Returns a JSON object containing a random patrol action"""
    if not request.session.get('deployed', False):
        return HttpResponseRedirect(reverse('deploy'))

    action = action()

    try:
        request.session['enemy'] = action.enemy.id
    except:
        pass

    data = {
        'action': action.serialize(),
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