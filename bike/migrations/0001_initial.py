# Generated by Django 4.1.7 on 2023-02-28 14:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('mode_name', models.CharField(max_length=150)),
                ('colors', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('price', models.CharField(max_length=50)),
                ('mpg', models.CharField(max_length=200)),
                ('radio', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('qty', models.CharField(max_length=200)),
                ('bike_image', models.ImageField(blank=True, default='x-adv.jpg', null=True, upload_to='bike_images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]