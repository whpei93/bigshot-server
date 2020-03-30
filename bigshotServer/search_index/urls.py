from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .viewsets.movie import MovieDocumentView

router = DefaultRouter()
movies = router.register(r'movies',
                        MovieDocumentView,
                        basename='moviedocument')

urlpatterns = [
    url(r'^', include(router.urls)),
]