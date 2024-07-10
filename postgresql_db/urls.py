from django.urls import path
from .views import check_postgresql_connection

urlpatterns = [
    path('', check_postgresql_connection, name='check_mysql_connection'),
]
