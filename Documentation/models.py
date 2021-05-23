from django.db import models
from django.utils import timezone


# Create your models here.
class Docs(models.Model):
    nombre = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    created = models.DateTimeField(default=timezone.now())

class Rating(models.Model):
    RATINGS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    web = models.ForeignKey(Docs, on_delete=models.CASCADE, related_name='documents')
    rating = models.CharField(choices=RATINGS, null=True, blank=True, max_length=1)
    comentario = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now())

