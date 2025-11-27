from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from .models import Autor, Libro, Resena
from .serializers import AutorSerializer, LibroSerializer, ResenaSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["autor","fecha_publicacion"]
    ordering_fields = ["fecha_publicacion", "titulo"]

    # endpoint extra
    @action(detail=True, methods=["get"])
    def promedio(self, request, pk=None):
        libro = self.get_object()
        promedio = libro.resenas.aggregate(Avg("calificacion"))["calificacion__avg"]
        return Response({"promedio": promedio})


class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
