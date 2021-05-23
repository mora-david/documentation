from django.test import TestCase
from Documentation.models import Docs, Rating


# Create your tests here.

class DocumentatioTests(TestCase):
    url = '/api/Documentation/'

    def test_getDocumentation(self):
        """
        Test get general
        """
        r = self.client.get(self.url)
        self.assertEqual(r.status_code, 200)

    def test_postDocumentation(self):
        """
        test para el create de documentación, hace post con la data, nombre, web, url y descripcion
        """
        data = {'nombre': 'django', 'web': 'https://www.djangoproject.com/', 'url': 'https://www.djangoproject.com/',
                'descripcion': 'documentación oficial de django'}

        r = self.client.post(self.url, data)
        self.assertEqual(r.status_code, 201)

        Documentacion = Docs.objects.get(pk=1)
        self.assertEqual(Documentacion.descripcion, 'documentación oficial de django')

    def test_updateDocumentation(self):
        """
        test para el update de un elemento previamente creado en documentación
        """
        doc = Docs.objects.create(nombre='doc1', web="web1.com", url="www.django.com", descripcion="oficial1")
        data = {'nombre': 'django', 'web': 'https://www.djangoproject.com/', 'url': 'https://www.djangoproject.com/',
                'descripcion': 'documentación oficial de django'}
        r = self.client.put(self.url + '1/', data, content_type='application/json')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(Docs.objects.get(pk=doc.pk).nombre, 'django')

    def test_deleteDocumentation(self):
        """
        Test para el delete de Documentation
        """
        doc = Docs.objects.create(nombre='doc1', web="web1.com", url="www.django.com", descripcion="oficial1")
        self.assertEqual(Docs.objects.count(), 1)
        r = self.client.delete(self.url + '1/')
        self.assertEqual(r.status_code, 204)
        self.assertEqual(Docs.objects.count(), 0)

    def test_get_with_rating_and_comments(self):
        """
        El test evalúa que el endpoint regrese en el get los comentarios, votos y un promedio del rating
        """

        doc = Docs.objects.create(nombre='doc1', web="web1.com", url="www.django.com", descripcion="oficial1")
        rt = Rating.objects.create(web=doc, rating=4, comentario='comentario original')
        rt2 = Rating.objects.create(web=doc, rating=2, comentario='comentario 2')
        r = self.client.get(self.url)
        self.assertEqual(r.data[0]['review'][0]['comentario'], 'comentario original')
        self.assertEqual(r.data[0]['calificacion_promedio'], 3)

class RateDocs(TestCase):
    url = '/api/Rating/'

    def test_getRating(self):
        """
        Test general para get de rating
        """
        r = self.client.get(self.url)
        self.assertEqual(r.status_code,200)

    def test_postRating(self):
        """
        test con el cual se genera un nuevo voto y comentario (opcional), hacía alguna documentación
        """
        doc = Docs.objects.create(nombre='doc1', web="web1.com", url="www.django.com", descripcion="oficial1")
        data = {'web':'1', 'rating':'5','comentario':'docs muy completos'}
        r = self.client.post(self.url, data)
        self.assertEqual(r.status_code,201)
        self.assertEqual(Rating.objects.get(pk=1).comentario,'docs muy completos')
        self.assertEqual(Rating.objects.get(pk=1).web.nombre,'doc1')

    def test_updateRating(self):
        """
        test para validar laactualización de un voto o documentación
        """
        doc = Docs.objects.create(nombre='doc1', web="web1.com", url="www.django.com", descripcion="oficial1")
        rt = Rating.objects.create(web=doc, rating=4, comentario='comentario original')
        data = {'web':'1', 'rating': '5', 'comentario': 'comentario actualizado'}
        r = self.client.put(self.url + '1/', data, content_type='application/json')
        self.assertEqual(r.status_code, 200)

    def test_delete_updateRating(self):
        """
        test para validar que se borren los votos o comentarios
        """
        doc = Docs.objects.create(nombre='doc1', web="web1.com", url="www.django.com", descripcion="oficial1")
        rt = Rating.objects.create(web=doc, rating=4, comentario='comentario original')
        self.assertEqual(Rating.objects.count(),1)
        r = self.client.delete(self.url + '1/')
        self.assertEqual(r.status_code, 204)
        self.assertEqual(Rating.objects.count(), 0)





