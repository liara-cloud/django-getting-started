# photos/views.py

from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_uploaded_photo')
    else:
        form = PhotoForm()
    return render(request, 'photos/upload_photo.html', {'form': form})

def show_uploaded_photo(request):
    latest_photo = Photo.objects.last()  # Retrieve the latest uploaded photo
    return render(request, 'photos/show_uploaded_photo.html', {'photo': latest_photo})
