# Generated by Django 5.0.2 on 2024-05-18 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_rename_problemacompletado_problemaaceptado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problemaaceptado',
            old_name='fecha_completado',
            new_name='fecha_aceptado',
        ),
    ]
