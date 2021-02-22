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
    request.session['enemy'] = None

    return render(request, "index.html")


@login_required
def workshop(request):
    """The workshop area where a user may look at their mech in closer detail"""
    try:
        mech = getMechByUser(request)
    
    except:
        mech = None

    request.session['deployed'] = False
    request.session['enemy'] = None

    return render(request, 'workshop.html', {'mech': mech})


@login_required
def equipment_all(request):
    """An equipment area where a user may look at all of their equipment
    and perform repairs if necessary"""
    request.session['deployed'] = False
    request.session['enemy'] = None

    return render(request, 'equipment-all.html')


@login_required
def store(request):
    """A place where users may purchase new equipment"""
    request.session['deployed'] = False
    request.session['enemy'] = None

    return render(request, 'store.html')


@login_required
def deploy(request):
    """The launching area for patrols"""
    try:
        mech = getMechByUser(request)
    except:
        return HttpResponseRedirect(reverse('workshop'))

    request.session['mech'] = mech.id
    request.session['deployed'] = True
    request.session['enemy'] = None

    return render(request, 'deploy.html')
