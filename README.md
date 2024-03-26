# Django App Using PostgreSQL Connection Pooling

## Installation (Local)

```
git clone https://github.com/liara-cloud/django-getting-started.git
```
```
cd django-getting-started
```
```
git checkout db-connection-pool
```
```
pip install virtualenv
```
```
python -m venv .venv
```
```
source .venv/Scripts/activate # .venv\Scripts\activate in Windows
```
```
pip install -r requirements.txt
```
```
cp .env.example .env # or rename .env.example to .env in Windows
```
- set your PostgreSQL ENVs in .env file

```
python manage.py makemigrations
python manage.py migrate
```
```
python manage.py runserver
```

## Installation ([Liara](https://liara.ir))
```
git clone https://github.com/liara-cloud/django-getting-started.git
```
```
cd django-getting-started
```
```
git checkout db-connection-pool
```
- create django app on [Liara](https://console.liara.ir/apps/create)
- set your PostgreSQL Envs in [app -> settings -> Variables](https://docs.liara.ir/app-deploy/django/envs/)

```
npm install -g @liara/cli
```
```
liara login
```
```
liara deploy
```

- after deploying, go to app -> CommandLine, then execute these commands:
```
python manage.py makemigrations
python manage.py migrate
```

## Documentation
- Persian: [Liara]()
- English: [Psycopg](https://www.psycopg.org/psycopg3/docs/basic/install.html#installing-the-connection-pool)



