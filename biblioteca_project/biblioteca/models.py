from django.db import models
from django.core.exceptions import ValidationError


def validar_nombre_autor(nombre):
    if not nombre or nombre.strip() == "":
        raise ValidationError("El nombre del autor no puede estar vacío o solo espacios.")

def validar_resumen(resumen):
    if len(resumen) < 50:
        raise ValidationError("El resumen debe tener al menos 50 caracteres.")

def validar_calificacion(valor):
    if valor < 0.0 or valor > 5.0:
        raise ValidationError("La calificación debe estar entre 0.0 y 5.0.")


class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre_autor])
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[validar_resumen])
    
    def __str__(self):
        return self.titulo


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    calificacion = models.IntegerField(validators=[validar_calificacion])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - ({self.calificacion}/5)"
