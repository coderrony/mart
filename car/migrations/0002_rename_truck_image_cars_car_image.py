# Generated by Django 4.1.7 on 2023-02-28 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='truck_image',
            new_name='car_image',
        ),
    ]