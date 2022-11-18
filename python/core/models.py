from django.db import models

class Equipo (models.Model):
    nameoftheteam= models.CharField (max_length=100, verbose_name='NOMBRE DEL EQUIPO')
    teamImage = models.ImageField (verbose_name='escudo')
    Teamshield = models.ImageField (verbose_name='bandera')


    def str(self) :
        return self.description

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        db_table = 'equipos'
        ordering = ['id']

class Jugador (models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre')
    lastName = models.CharField (max_length=100, verbose_name='Apellido')
    playerImage = models.ImageField (verbose_name='Foto')
    Dateofbirth=models.DateTimeField (verbose_name='Fecha de Nacimiento')
    jerseynumber = models.PositiveIntegerField(verbose_name='Numero de camisa')
    headline = models.BooleanField(verbose_name='Es titular?')
    Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name='Equipo')


    def str(self) :
        return self.description

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        db_table = 'jugador'
        ordering = ['id']

class Posicion (models.Model):
    name = models.CharField(max_length=100, verbose_name='Posicion')
    description = models.CharField (max_length=100, verbose_name='Descripcion')

    def str(self) :
        return self.description

    class Meta:
        verbose_name = 'Posicion'
        verbose_name_plural = 'Posiciones'
        db_table = 'pocision'
        ordering = ['id']


class Tecnico (models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre')
    lastName = models.CharField (max_length=100, verbose_name='Apellido')
    Dateofbirth=models.DateTimeField (verbose_name='Fecha de Nacimiento')
    Rol = models.CharField(max_length=100, verbose_name='Rol')

    def str(self) :
        return self.description

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        db_table = 'tecnico'
        ordering = ['id']

    