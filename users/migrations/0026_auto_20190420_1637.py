# Generated by Django 2.2 on 2019-04-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20190419_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasaje',
            name='NotificacionDia',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='pasaje',
            name='NotificacionHoras',
            field=models.IntegerField(default='0'),
        ),
    ]
