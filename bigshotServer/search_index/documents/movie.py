from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from movies.models import Movie

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

@INDEX.doc_type
class MovieDocument(Document):
    title = fields.TextField()
    id = fields.IntegerField()
    stars = fields.IntegerField()
    class Django(object):
        model = Movie