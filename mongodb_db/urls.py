from django.urls import path
from .views import check_mongodb_connection

urlpatterns = [
    path('', check_mongodb_connection, name='check_mongodb_connection'),
]
