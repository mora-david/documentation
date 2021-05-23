from django.db import models
from django.utils import timezone


# Create your models here.
class Docs(models.Model):
    """
    id -> autoincrementable
    Modelo principal donde se guarda la info sobre la documentación:
    nombre -> nombre del sitio ej: Django
    web -> web oficial de Django
    url -> www.django.com
    descripcion: documentación oficial de django
    created -> autogenerado la fecha en que se crea el elemento
    """
    nombre = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    created = models.DateTimeField(default=timezone.now())

class Rating(models.Model):
    """
        id -> autoincrementable
        Modelo principal donde se guarda la info sobre la documentación:
        web -> llave foranea hacía el modelo de Docs eje: 1
        rating -> valor de calificación del 1 al 5
        comentario -> comentario asociado a la valoración es opcional
        created -> autogenerado la fecha en que se crea el elemento
        """
    RATINGS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    web = models.ForeignKey(Docs, on_delete=models.CASCADE, related_name='documents')
    rating = models.CharField(choices=RATINGS, null=True, blank=True, max_length=1)
    comentario = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now())

