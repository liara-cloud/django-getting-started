from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

def check_mongodb_connection(request):
    try:
        client = MongoClient('mongodb://root:AOnj2OEXiUkgNk2B1tL23gA9@bromo.liara.cloud:30126/my-app?authSource=admin')
        client.admin.command('ping')
        return HttpResponse("MongoDB connection successful")
    except Exception as e:
        return HttpResponse(f"MongoDB connection failed: {e}")
