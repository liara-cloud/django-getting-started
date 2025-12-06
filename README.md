# Send Email Using Django (Liara)
## Steps
```
git clone https://github.com/liara-cloud/django-getting-started.git
```
```
cd django-getting-started
```
```
git checkout email-server
```
```
mv .env.example .env # and set ENVs
```
```
pip install virtualenv
```
```
python -m venv .venv 
```
```
source .venv\Scripts\Activate # source .venv/bin/activate
```
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py runserver
```
- check `http://127.0.0.1:8000/send-test-email`

## Need More Info?
- [Liara Docs](https://docs.liara.ir/email-server/how-tos/connect-via-platform/django/)
- [Django Mail Docs](https://docs.djangoproject.com/en/5.1/topics/email/)
