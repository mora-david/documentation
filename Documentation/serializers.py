from Documentation.models import Docs, Rating
from rest_framework import serializers
from django.db.models import Avg

class RatingSerializer(serializers.ModelSerializer):
    """
    Serializador para mostrar la valoración del 1 al 5 y los comentarios asociados a la documentación, se utiliza
    para el CRUD del modelo Rating
    """

    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['created']

class DocsSerializer(serializers.ModelSerializer):
    """
    Serializador utilizado para la documentación, se utiliza para el crud, cuando se usa para el get, devuelve además
    los rating y comentarios asociados a dicha documentación
    """
    review = serializers.SerializerMethodField()
    calificacion_promedio = serializers.SerializerMethodField()
    # review = RatingSerializer
    class Meta:
        model = Docs
        fields= ('nombre','web','url','descripcion','created','review','calificacion_promedio')
        read_only_fields = ['created']

    def get_review(self, obj):
        reviews = Rating.objects.filter(web=obj.id)
        serializer =  RatingSerializer(reviews, many=True)
        return serializer.data

    def get_calificacion_promedio(self, obj):
        cal = Rating.objects.filter(web=obj.id).aggregate(Avg('rating'))["rating__avg"]
        return cal