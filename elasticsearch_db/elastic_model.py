from elasticsearch import Elasticsearch
from django.conf import settings

class ElasticModel:
    def __init__(self):
        self.client = Elasticsearch(settings.ELASTICSEARCH_DSL['default']['hosts'])
        self.index = 'test_index'

    def create_index(self):
        if not self.client.indices.exists(index=self.index):
            self.client.indices.create(index=self.index)

    def insert_data(self, data):
        self.client.index(index=self.index, document=data)

    def read_data(self):
        response = self.client.search(index=self.index, body={"query": {"match_all": {}}})
        return response['hits']['hits']
