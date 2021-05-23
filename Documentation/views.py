from rest_framework import viewsets, status
from rest_framework. response import Response
from Documentation.serializers import DocsSerializer, RatingSerializer
from Documentation.models import Docs, Rating


class DocsViewSet(viewsets.ModelViewSet):
    serializer_class = DocsSerializer
    queryset = Docs.objects.all()

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

