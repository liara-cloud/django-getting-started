from django.shortcuts import render
import os
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    logger.info('Everything is OK!')
    return render(request, "index.html")


def envs(request):
    print(os.getenv('LIARA_URL', 'LIARA_URL is not set.'), flush=True)
    return render(request, "index.html")
