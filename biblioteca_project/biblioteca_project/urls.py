from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from biblioteca.viewsets import AutorViewSet, LibroViewSet, ResenaViewSet

router = DefaultRouter()
router.register("autores", AutorViewSet, basename="autores")
router.register("libros", LibroViewSet, basename="libros")
router.register("resenas", ResenaViewSet, basename="resenas")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/", include("students.urls")),

]
