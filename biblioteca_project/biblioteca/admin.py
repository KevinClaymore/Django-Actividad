from django.contrib import admin
from .models import Autor, Libro, Resena

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','autor', 'fecha_publicacion', 'resumen')
    search_fields = ('titulo','autor__nombre')
    list_filter = ('autor',)

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('id','libro','calificacion', 'fecha','texto')
    search_fields = ('libro__titulo',)
    list_filter = ('calificacion',)
