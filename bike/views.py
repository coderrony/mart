from django.shortcuts import render

# Create your views here.
def bikePage(request):
    return render(request, 'bike.html', {})