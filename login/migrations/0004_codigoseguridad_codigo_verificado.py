# Generated by Django 5.0.2 on 2024-07-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_codigoseguridad'),
    ]

    operations = [
        migrations.AddField(
            model_name='codigoseguridad',
            name='codigo_verificado',
            field=models.BooleanField(default=False),
        ),
    ]
