from django.shortcuts import render
from .models import SpareParts

# Create your views here.

def spareParts(request):
    spareParts = SpareParts.objects.all()
    return render(request, 'spareParts.html',context={'spareParts': spareParts})