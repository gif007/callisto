from django.shortcuts import render
from .models import MobileSuit

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