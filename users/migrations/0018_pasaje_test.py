# Generated by Django 2.2 on 2019-04-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_customuser_es_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasaje',
            name='test',
            field=models.BooleanField(default=False),
        ),
    ]
