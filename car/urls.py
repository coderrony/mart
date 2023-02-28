from django.urls import path
from . import views


urlpatterns = [
    path('', views.carPage, name="car"),
]