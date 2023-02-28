from django.shortcuts import render
from .models import Cars_inventory

# Create your views here.
def carPage(request):
    return render(request, 'car.html', {})

# def car_inventory(request):
#     car_inventory = car_inventory.objects.all()
#     return render(request, car_inventory)
    