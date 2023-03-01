from django.shortcuts import render
from .models import Cars
# Create your views here.


def carPage(request):
    cars = Cars.objects.all()
    return render(request, 'car.html', context={'cars': cars})
