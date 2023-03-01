from django.shortcuts import render
from .models import Bikes
# Create your views here.


def bikePage(request):
    bikes = Bikes.objects.all()
    return render(request, 'bike.html', {'bikes': bikes})
