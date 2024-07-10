from django.shortcuts import HttpResponse
import redis

def check_redis_connection(request):
    try:
        # Connect to Redis
        redis_url = 'redis://:z4cLHblJzYJcIZk73OGeqyIz@bromo.liara.cloud:30664/0'
        r = redis.StrictRedis.from_url(redis_url)

        # Insert data
        r.set('test_key', 'test_value')

        # Read data
        value = r.get('test_key')

        return HttpResponse(f"Redis operation successful, value: {value.decode('utf-8')}")
    except Exception as e:
        return HttpResponse(f"Redis operation failed: {e}")
