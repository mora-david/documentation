from Documentation.models import Docs, Rating
from rest_framework import serializers
from django.db.models import Avg

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['created']

class DocsSerializer(serializers.ModelSerializer):
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