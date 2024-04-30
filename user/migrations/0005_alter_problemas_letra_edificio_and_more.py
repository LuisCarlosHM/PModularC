# Generated by Django 5.0.2 on 2024-04-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_areascomunes_id_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemas',
            name='letra_edificio',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='problemas',
            name='numero_salon',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problemas',
            name='piso_baño',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='problemas',
            name='tipo_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='problemas',
            name='tipo_baño',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='problemas',
            name='tipo_departamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='problemas',
            name='tipo_edificio_departamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='problemas',
            name='ubicacion_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='problemas',
            name='ubicacion_departamento',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problemas',
            name='ubicacion_exacta',
            field=models.TextField(blank=True, null=True),
        ),
    ]