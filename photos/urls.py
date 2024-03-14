# photos/urls.py

from django.urls import path, re_path
from .views import upload_photo, download_photo, delete_photo

urlpatterns = [
    path('', upload_photo, name='upload_photo'),
    re_path(r'^download/(?P<photo_name>.+)/$', download_photo, name='download_photo'),
    re_path(r'^delete/(?P<photo_name>.+)/$', delete_photo, name='delete_photo'),  # Update this line
]
