from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse

def check_mssql_connection(request):
    try:
        connection = connections['mssql']
        connection.ensure_connection()
        return HttpResponse("MSSQL connection successful")
    except Exception as e:
        return HttpResponse(f"MSSQL connection failed: {e}")
