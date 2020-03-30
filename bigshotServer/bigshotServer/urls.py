from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from search_index import urls as search_index_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^search/', include(search_index_urls)),
]