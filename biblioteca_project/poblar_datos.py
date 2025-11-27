from biblioteca.models import Autor, Libro, Resena
from datetime import date

a1 = Autor.objects.create(nombre="Lee Child", nacionalidad="Reino Unido")
a2 = Autor.objects.create(nombre="Clive Cussler", nacionalidad="Estados Unidos")
a3 = Autor.objects.create(nombre="John Grisham", nacionalidad="Estados Unidos")
a4 = Autor.objects.create(nombre="Michael Crichton", nacionalidad="Estados Unidos")
a5 = Autor.objects.create(nombre="Gillian Flynn", nacionalidad="Estados Unidos")

l1 = Libro.objects.create(
    titulo="Zona Peligrosa",
    autor=a1,
    fecha_publicacion=date(1997, 3, 17),
    resumen="Jack Reacher llega a una pequeña ciudad donde descubre una red criminal peligrosa."
)

l2 = Libro.objects.create(
    titulo="El Oro del Rey",
    autor=a2,
    fecha_publicacion=date(2003, 6, 10),
    resumen="Dirk Pitt se enfrenta a un conflicto internacional mientras busca un tesoro perdido."
)

l3 = Libro.objects.create(
    titulo="El Informe Pelícano",
    autor=a3,
    fecha_publicacion=date(1992, 10, 15),
    resumen="Una estudiante de derecho descubre secretos que la ponen en la mira de asesinos influyentes."
)

l4 = Libro.objects.create(
    titulo="Esfera",
    autor=a4,
    fecha_publicacion=date(1987, 9, 22),
    resumen="Un equipo de científicos desciende al fondo del océano para investigar una nave misteriosa."
)

l5 = Libro.objects.create(
    titulo="Perdida",
    autor=a5,
    fecha_publicacion=date(2012, 5, 24),
    resumen="El marido de una mujer desaparecida se convierte en el principal sospechoso en un caso lleno de giros."
)

Resena.objects.create(libro=l1, texto="Muy buena historia, mantiene el suspenso.", calificacion=4)
Resena.objects.create(libro=l1, texto="Reacher siempre cumple en acción.", calificacion=5)

Resena.objects.create(libro=l2, texto="Aventura pura, fácil de leer.", calificacion=4)
Resena.objects.create(libro=l2, texto="Me gustó el ritmo.", calificacion=4)

Resena.objects.create(libro=l3, texto="Grisham nunca decepciona.", calificacion=5)
Resena.objects.create(libro=l3, texto="Intriga jurídica muy bien escrita.", calificacion=4)

Resena.objects.create(libro=l4, texto="Tiene ideas muy buenas, algo lento al inicio.", calificacion=3)
Resena.objects.create(libro=l4, texto="Crichton siempre mezcla ciencia con acción.", calificacion=5)

Resena.objects.create(libro=l5, texto="Tremendo thriller psicológico.", calificacion=5)
Resena.objects.create(libro=l5, texto="Los giros son brutales.", calificacion=5)

print("Datos cargados.")
