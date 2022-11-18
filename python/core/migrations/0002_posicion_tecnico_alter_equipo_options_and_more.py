# Generated by Django 4.1.3 on 2022-11-06 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Posicion')),
                ('description', models.CharField(max_length=100, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Posicion',
                'verbose_name_plural': 'Posiciones',
                'db_table': 'pocision',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('lastName', models.CharField(max_length=100, verbose_name='Apellido')),
                ('Dateofbirth', models.DateTimeField(verbose_name='Fecha de Nacimiento')),
                ('Rol', models.CharField(max_length=100, verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'Tecnico',
                'verbose_name_plural': 'Tecnicos',
                'db_table': 'tecnico',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='equipo',
            options={'ordering': ['id'], 'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AlterField(
            model_name='equipo',
            name='teamImage',
            field=models.ImageField(upload_to='', verbose_name='escudo'),
        ),
        migrations.AlterModelTable(
            name='equipo',
            table='equipos',
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('lastName', models.CharField(max_length=100, verbose_name='Apellido')),
                ('playerImage', models.ImageField(upload_to='', verbose_name='Foto')),
                ('Dateofbirth', models.DateTimeField(verbose_name='Fecha de Nacimiento')),
                ('jerseynumber', models.PositiveIntegerField(verbose_name='Numero de camisa')),
                ('headline', models.BooleanField(verbose_name='Es titular?')),
                ('Equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipo', verbose_name='Equipo')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
                'db_table': 'jugador',
                'ordering': ['id'],
            },
        ),
    ]