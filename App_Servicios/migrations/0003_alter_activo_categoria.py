# Generated by Django 4.1.6 on 2023-02-16 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Servicios', '0002_alter_servicio_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='categoria',
            field=models.CharField(max_length=20),
        ),
    ]
