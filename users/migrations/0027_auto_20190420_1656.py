# Generated by Django 2.2 on 2019-04-20 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20190420_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasaje',
            name='NotificacionDia',
        ),
        migrations.RemoveField(
            model_name='pasaje',
            name='NotificacionHoras',
        ),
        migrations.AddField(
            model_name='pasaje',
            name='NotificacionDiaEnv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pasaje',
            name='NotificacionHorasEnv',
            field=models.BooleanField(default=False),
        ),
    ]
