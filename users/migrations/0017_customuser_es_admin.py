# Generated by Django 2.2 on 2019-04-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_delete_administrador'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='es_admin',
            field=models.BooleanField(default=False),
        ),
    ]
