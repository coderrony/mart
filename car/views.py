from django.shortcuts import render

# Create your views here.
def carPage(request):
    return render(request, 'car.html', {})