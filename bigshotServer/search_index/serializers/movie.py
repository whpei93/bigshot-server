from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from ..documents.movie import MovieDocument


class MovieDocumentSerializer(DocumentSerializer):
    class Meta(object):
        document = MovieDocument