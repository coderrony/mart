# Generated by Django 4.1.7 on 2023-02-28 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_rename_mode_name_cars_model_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='model_name',
            new_name='mode_name',
        ),
    ]