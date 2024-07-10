from django.urls import path
from .views import elasticsearch_insert_read

urlpatterns = [
    path('', elasticsearch_insert_read, name='elasticsearch_insert_read'),
]
