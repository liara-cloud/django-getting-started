from django.shortcuts import render
from psycopg_pool import ConnectionPool
import random, string

def index(request):
    with ConnectionPool(conninfo='postgresql://root:cIdX6SQawIaWScOKpFBcel1v@olympus.liara.cloud:34464/postgres') as pool:
        with pool.connection() as conn:
            with conn.cursor() as cursor:
                for _ in range(10):
                    data = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                    cursor.execute("INSERT INTO myapp_testmodel (data) VALUES (%s)", [data])

            with conn.cursor() as cursor:
                cursor.execute("SELECT data FROM myapp_testmodel")
                data = [row[0] for row in cursor.fetchall()]
    
    return render(request, 'myapp/index.html', {'data': data})