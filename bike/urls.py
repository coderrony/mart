from django.urls import path
from . import views


urlpatterns = [
    path('', views.bikePage, name="bike"),
]
