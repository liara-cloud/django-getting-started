from django.shortcuts import render
from psycopg_pool import ConnectionPool
import random, string, os

if os.getenv('DEBUG') != 'false':
    from dotenv import load_dotenv
    load_dotenv()

def index(request):
    with ConnectionPool(conninfo=os.getenv('DB_URI')) as pool:
        pool.wait()
        with pool.connection() as conn:
            for _ in range(10):
                data = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                conn.execute("INSERT INTO myapp_testmodel (data) VALUES (%s)", [data])

            with conn.cursor() as cursor:
                cursor.execute("SELECT data FROM myapp_testmodel")
                data = [row[0] for row in cursor.fetchall()]
    
    return render(request, 'myapp/index.html', {'data': data})