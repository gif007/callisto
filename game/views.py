from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import permission_required

from .models import MobileSuit, Enemy
from .functions import *
from .data_structures import spam

"""
After testing is complete you will want to prepend each of these views with
the @login_required decorator
"""

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

def index(request):

    return render(request, "game.html")


def workshop(request):

    mech = get_mech_by_user(MobileSuit, User, request)

    return render(request, 'workshop.html', {'mech': mech})


def equipment(request):

    return render(request, 'equipment.html')


def store(request):

    return render(request, 'store.html')


def deploy(request):

    mech = get_mech_by_user(MobileSuit, User, request)
    request.session['mech'] = mech.id
    request.session['deployed'] = True

    return render(request, 'deploy.html', {'mech': mech})


def get_action(request, action=spam):

    # import random
    # action = random.choice(list(actions.values()))
    action = spam()
    mech = MobileSuit.objects.filter(id=request.session['mech']).get()

    try:
        enemy = Enemy.objects.filter(id=action['enemy']).get()
    except:
        enemy = None

    data = {
        'text': action['text'],
        'enemy': enemy.name if enemy else None,
        'mech': mech.name
    }

    return JsonResponse(data)
