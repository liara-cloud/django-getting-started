from django.shortcuts import render
import os

# Create your views here.


def index(request):
    return render(request, "index.html")


def envs(request):
    print(os.getenv('LIARA_URL', 'LIARA_URL is not set.'), flush=True)
    return render(request, "index.html")
