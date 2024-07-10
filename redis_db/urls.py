from django.urls import path
from .views import check_redis_connection

urlpatterns = [
    path('', check_redis_connection, name='check_redis_connection'),
]
