"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('user/', include('users.urls')),
<<<<<<< HEAD
    path('bike/', include('bike.urls')),
    path('car/', include('car.urls')),
    path('truck/', include('truck.urls')),
=======
    path('bike', include('bike.urls')),
    path('car', include('car.urls')),
>>>>>>> 2a01c7e670c667aa3603813f577d58e7cf1d6260
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
