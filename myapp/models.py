from django.db import models
import random
import string

class TestModel(models.Model):
    data = models.CharField(max_length=100)

    @classmethod
    def generate_random_data(cls):
        data = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        cls.objects.create(data=data)

    def __str__(self):
        return self.data