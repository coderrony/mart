from django.shortcuts import render

from .models import Trucks
# Create your views here.


def trucks(request):
    truck = Trucks.objects.all()
    return render(request, 'truck.html', context={'truck': truck})
