from django.urls import path
from . import views

urlpatterns = [
    path('', views.trucks, name='trucks'),

]
