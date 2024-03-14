## Installation (Local)
```
git clone https://github.com/liara-cloud/django-getting-started.git
```
```
cd django-getting-started
```
```
git checkout upload-s3
```
```
pip install virtualenv
```
```
python -m venv .venv
```
```
source .venv/Scripts/activate.bat # .venv\Scripts\activate in Windows
```
```
pip install -r requirements.txt
```
```
mv .env.example .env # or rename .env.example file to .env (in Windows)
```
- set ENVs based on your bucket info
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
