# Generated by Django 5.0.2 on 2024-04-20 17:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreasComunes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoArea', models.CharField(max_length=100)),
                ('UbicacionArea', models.CharField(max_length=100)),
                ('TipoProblema', models.CharField(max_length=100)),
                ('GravedadProblema', models.CharField(max_length=100)),
                ('DescripcionProblema', models.TextField()),
                ('UbicacionExacta', models.TextField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Baños',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_baño', models.CharField(max_length=100)),
                ('letra_edificio', models.CharField(max_length=100)),
                ('piso_baño', models.CharField(max_length=100)),
                ('tipo_problema', models.CharField(max_length=100)),
                ('gravedad_problema', models.CharField(max_length=100)),
                ('descripcion_problema', models.TextField()),
                ('ubicacion_exacta', models.TextField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoDepartamento', models.CharField(max_length=100)),
                ('TipoEdificio', models.CharField(blank=True, max_length=100)),
                ('UbicacionDepartamento', models.CharField(blank=True, max_length=100)),
                ('TipoProblema', models.CharField(max_length=100)),
                ('GravedadProblema', models.CharField(max_length=100)),
                ('DescripcionProblema', models.TextField()),
                ('UbicacionExacta', models.TextField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
