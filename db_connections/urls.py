from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysql/', include('mysql_db.urls')),
    path('mariadb/', include('mariadb_db.urls')),
    # path('postgresql/', include('postgresql_db.urls')),
    # path('mssql/', include('mssql_db.urls')),
    # path('mongodb/', include('mongodb_db.urls')),
    # path('elasticsearch/', include('elasticsearch_db.urls')),
    # path('rabbitmq/', include('rabbitmq.urls')),
]
