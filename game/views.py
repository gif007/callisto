from django.shortcuts import render
from .models import MobileSuit
from django.http import JsonResponse

# Create your views here.

def index(request):

    return render(request, "game.html")


def workshop(request):
    mechs = request.user.mobilesuit_set.all()

    return render(request, 'workshop.html', {'mechs': mechs})


def equipment(request):

    return render(request, 'equipment.html')


def store(request):

    return render(request, 'store.html')


def deploy(request):
    mech = request.user.mobilesuit_set.filter(active=True).get()

    return render(request, 'deploy.html', {'mech': mech})


def get_action(request):
    actions = [
        'A monster attacks!',
        'Nothing happens...',
        'You discover a cave!',
    ]

    import random
    action = actions[random.randint(0,2)]

    data = {
        'data': action
    }

    return JsonResponse(data)