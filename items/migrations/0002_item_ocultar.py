# Generated by Django 4.0.1 on 2022-02-08 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ocultar',
            field=models.BooleanField(default=True),
        ),
    ]
