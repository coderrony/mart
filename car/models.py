from django.db import models

# Create your models here.

class Cars_inventory(models.Model):
    name = models.CharField(blank = True,null = True, max_length = 200)
    description = models.TextField(blank=True, null=True)