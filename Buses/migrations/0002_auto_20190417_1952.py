# Generated by Django 2.2 on 2019-04-17 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='Patente',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
