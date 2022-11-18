from django.contrib import admin
from .models import Equipo,Tecnico,Posicion,Jugador
from django.utils.html import format_html

@admin.register(Equipo)
class EquipoAdmin (admin.ModelAdmin):
    list_display = ['nameoftheteam','bandera','escudo',]

    def bandera (self, obj):
        return format_html('<img src={} width="130" height="100"/>', obj.teamImage.url)

    def escudo (self, obj):
        return format_html('<img src={} width="130" height="100"/>', obj.Teamshield.url)

@admin.register(Tecnico)
class TecnicoAdmin (admin.ModelAdmin):
    list_display=['name','lastName','Dateofbirth','Rol']

@admin.register(Posicion)
class PosicionAdmin (admin.ModelAdmin):
    list_display=['name','description']

@admin.register(Jugador)
class JugadorAdmin (admin.ModelAdmin):
    list_display=['name','lastName','fotouwu','Dateofbirth','jerseynumber','headline','Equipo']
    
    def fotouwu (self, obj):
        return format_html('<img src={} width="130" height="100"/>', obj.playerImage.url)
