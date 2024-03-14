from django.urls import path
from .views import upload_photo, show_uploaded_photo

urlpatterns = [
    path('', upload_photo, name='upload_photo'),
    path('show/', show_uploaded_photo, name='show_uploaded_photo'),
]
