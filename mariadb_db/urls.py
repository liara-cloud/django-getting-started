from django.urls import path
from .views import check_mariadb_connection

urlpatterns = [
    path('', check_mariadb_connection, name='check_mariadb_connection'),
]
