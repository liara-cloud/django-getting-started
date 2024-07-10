from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse

def check_mariadb_connection(request):
    try:
        connection = connections['mariadb']
        connection.ensure_connection()
        return HttpResponse("MariaDB connection successful")
    except Exception as e:
        return HttpResponse(f"MariaDB connection failed: {e}")
