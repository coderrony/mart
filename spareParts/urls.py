from django.urls import path
from . import views

urlpatterns = [
    path('', views.spareParts, name="spareParts"),
]
