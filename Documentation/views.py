from rest_framework import viewsets
from Documentation.serializers import DocsSerializer, RatingSerializer
from Documentation.models import Docs, Rating


class DocsViewSet(viewsets.ModelViewSet):
    """
    Vista general de documentación
    """
    serializer_class = DocsSerializer
    queryset = Docs.objects.all()

class RatingViewSet(viewsets.ModelViewSet):
    """
    Vista general para revisar el rating de los comentarios
    """
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

