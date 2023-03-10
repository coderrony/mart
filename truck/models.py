
from django.db import models
import uuid
# Create your models here.


class Trucks(models.Model):
    mode_name = models.CharField(max_length=150)
    colors = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.CharField(max_length=50)
    mpg = models.CharField(max_length=200)
    radio = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    qty = models.CharField(max_length=200)
    truck_image = models.ImageField(
        null=True, blank=True, upload_to="truck_images/", default="coming-soon2.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.mode_name
