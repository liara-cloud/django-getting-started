# photos/views.py

from django.shortcuts import render, redirect
from .forms import PhotoForm

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_photo')
    else:
        form = PhotoForm()
    return render(request, 'photos/upload_photo.html', {'form': form})
