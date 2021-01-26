from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import permission_required
from django.urls import reverse

from .models import MobileSuit, Enemy, Helm, Chest, LeftArm, RightArm, Legs, Modifier
from .functions import *

"""
How to use the permissions decorator:
@permission_required('app.permission_name')
"""

"""
Normally you will want the PermissionRequiredMixin behavior:
return 403 if a user is logged in but does not have the correct permission.
To do this for a function view use @login_required and @permission_required
with raise_exception=True as shown:

@login_required
@permission_required('app.permission_name', raise_exception=True)
"""

# Create your views here.

@login_required
def index(request):
    """Literaly nothing"""
    request.session['deployed'] = False

    return render(request, "game.html")


@login_required
def workshop(request):
    """The workshop area where a user may look at their mech in closer detail"""
    mech = getMechByUser(request)
    request.session['deployed'] = False

    return render(request, 'workshop.html', {'mech': mech})


@login_required
def equipment_all(request):
    """An equipment area where a user may look at all of their equipment
    and perform repairs if necessary"""
    request.session['deployed'] = False

    return render(request, 'equipment-all.html')


@login_required
def equipment(request, typ, pk):
    """Shows an individual piece of equipment"""

    types = {
        'helm': Helm,
        'chest': Chest,
        'leftarm': LeftArm,
        'rightarm': RightArm,
        'legs': Legs,
        'modifier': Modifier,
    }

    piece = types[typ].objects.filter(id=pk).get()
    context = {
        'piece': piece,
        'type': typ,
    }
    
    return render(request, 'equipment.html', context=context)


@login_required
def store(request):
    """A place where users may purchase new equipment"""
    request.session['deployed'] = False
    return render(request, 'store.html')


@login_required
def deploy(request):
    """The launching area for patrols"""
    mech = getMechByUser(request)
    request.session['mech'] = mech.id
    request.session['deployed'] = True
    request.session['enemy'] = None

    return render(request, 'deploy.html', {'mech': mech})


@login_required
def get_action(request, action=randomAction):
    """Returns a JSON object containing a random patrol action"""
    if not request.session.get('deployed', False):
        return HttpResponseRedirect(reverse('deploy'))

    action = randomAction()
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
def flee(request):
    """Defines a redirect for leaving the outlands"""
    request.session['deployed'] = False
    request.session['enemy'] = None
    
    return HttpResponseRedirect(reverse('workshop'))
