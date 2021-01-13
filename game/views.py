from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "game.html")


def workshop(request):
    return render(request, 'workshop.html')


def equipment(request):
    return render(request, 'equipment.html')


def store(request):
    return render(request, 'store.html')