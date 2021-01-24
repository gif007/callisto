from django.shortcuts import render
from .models import MobileSuit
from django.http import JsonResponse

# Create your views here.

def index(request):

    return render(request, "game.html")


def workshop(request):
    
    mech = MobileSuit.objects.filter(
        controller=User.objects.filter(
        username=request.user.get_username()
        ).get()
        ).get()

    return render(request, 'workshop.html', {'mech': mech})


def equipment(request):

    return render(request, 'equipment.html')


def store(request):

    return render(request, 'store.html')


from django.contrib.auth.models import  User
def deploy(request):

    mech = MobileSuit.objects.filter(
        controller=User.objects.filter(
        username=request.user.get_username()
        ).get()
        ).get()

    return render(request, 'deploy.html', {'mech': mech})


from .data_structures import actions
def get_action(request, actions=actions):

    import random
    action = random.choice(list(actions.keys()))

    data = {
        'text': actions[action]['text'],
        'monster': actions[action]['monster'],
    }

    return JsonResponse(data)
