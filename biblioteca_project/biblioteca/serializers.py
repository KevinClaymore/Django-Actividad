from rest_framework import serializers
from .models import Autor, Libro, Resena

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = "__all__"


class LibroSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="autor.nombre")
    recent_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = "__all__"

    def get_recent_reviews(self, obj):
        reviews = obj.resenas.order_by("-fecha")[:5]
        return ResenaSerializer(reviews, many=True).data
 # SerializerMethodField permite agregar campos calculados dinámicamente.
 # En este caso muestra cuántas reseñas tiene un libro.