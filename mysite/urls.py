
from django.contrib import admin
from django.urls import path
from objectstorage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.manage_files, name='manage_files'),
    path('api/files/list/', views.list_files, name='list_files'),
    path('api/files/upload/', views.upload_file, name='upload_file'),
    path('api/files/delete/', views.delete_file, name='delete_file'),
    path('api/files/presigned-url/', views.generate_presigned_url, name='generate_presigned_url'),
]