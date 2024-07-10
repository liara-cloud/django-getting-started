from django.urls import path
from .views import check_mysql_connection

urlpatterns = [
    path('', check_mysql_connection, name='check_mysql_connection'),
]
