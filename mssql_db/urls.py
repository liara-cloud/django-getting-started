from django.urls import path
from .views import check_mssql_connection

urlpatterns = [
    path('', check_mssql_connection, name='check_mssql_connection'),
]
