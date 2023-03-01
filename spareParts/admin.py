from django.contrib import admin
from .models import SpareParts
# Register your models here.

from spareParts.models import SpareParts

class SparePartsAdmin(admin.ModelAdmin):
    list_display=('mode_name','colors','year','price','engine')


admin.site.register(SpareParts,SparePartsAdmin)
