from django.http import JsonResponse
from .elastic_model import ElasticModel
import json

def elasticsearch_insert_read(request):
    es_model = ElasticModel()
    es_model.create_index()
    
    # Insert data
    data = {
        'name': 'Sample Data',
        'description': 'This is a sample data entry for Elasticsearch.'
    }
    es_model.insert_data(data)
    
    # Read data
    results = es_model.read_data()
    
    return JsonResponse(results, safe=False)
