from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
# from django.contrib.auth.models import  User
# from django.contrib.auth.decorators import permission_required
from django.urls import reverse

from .models import MobileSuit, Enemy, Helm, Chest, LeftArm, RightArm, Legs, Modifier
from .functions import randomAction


@login_required
def get_action(request, action=randomAction):
    """Returns a JSON object containing a random patrol action"""
    if not request.session.get('deployed', False):
        return HttpResponseRedirect(reverse('deploy'))

    action = action()
    mech = MobileSuit.objects.filter(id=request.session['mech']).get()
    enemy = action['enemy']
    
    if enemy:
        request.session['enemy'] = enemy.id

    data = {
        'text': action['text'],
        'enemy': enemy.name if enemy else enemy,
        'mech': mech.name
    }

    return JsonResponse(data)


@login_required
def attack(request):
    """Beast mode"""
    mech = MobileSuit.objects.filter(id=request.session['mech']).get()
    enemy = Enemy.objects.filter(id=request.session['enemy']).get()

    mech_health = '%s/%s' % (mech.current_hp, mech.max_hp)
    enemy_health = '5/5'

    data = {
        'mech_health': mech_health,
        'enemy_': enemy_health,
    }

    return JsonResponse(data)


@login_required
def flee(request):
    """Defines a redirect for leaving the outlands"""
    request.session['deployed'] = False
    request.session['enemy'] = None
    
    return HttpResponseRedirect(reverse('workshop'))