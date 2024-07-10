from django.shortcuts import HttpResponse
from django.db import connections

def check_mysql_connection(request):
    try:
        with connections['mysql'].cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        if result:
            return HttpResponse("MySQL connection successful")
        else:
            return HttpResponse("MySQL connection failed")
    except Exception as e:
        return HttpResponse(f"MySQL connection failed: {e}")
