# Asynchronous Server Gateway Interface App
## Installation (Local)
```
git clone https://github.com/liara-cloud/django-getting-started.git
```
```
git checkout asgi
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
python manage.py makemigrations
```
```
python manage.py migrate
```
```
cp .env.example .env # or rename .env.example to .env in Windows 
```
- set your ENVs (especially REDIS_URI or use InMemoryChannelLayer)
  
```
python manage.py createsuperuser # create your own superuser
```
```
python manage.py runserver
```

## Installation (Liara)
```
git clone https://github.com/liara-cloud/django-getting-started.git
```
```
git checkout asgi
```
- create Django App on [Liara](https://console.liara.ir/apps/create)
- create Redis on [Liara](https://console.liara.ir/databases/create)
- create Disk Named database in Django App on Liara
- set REDIS_URI ENV in Django App on Liara
  
```
npm install -g @liara/cli
```
```
liara login
```
```
liara deploy
```
```
python manage.py createsuperuser # create your own superuser on CommandLine on Liara
```
