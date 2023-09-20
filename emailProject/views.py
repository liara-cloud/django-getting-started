# views.py

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

success_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ارسال موفقیت‌آمیز</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            margin: 100px auto;
            max-width: 600px;
            padding: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
        }
        h1 {
            color: #007bff;
            font-size: 2em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2em;
            color: #333;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            font-size: 1em;
            color: #fff;
            background-color: #007bff;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Email has been sent successfully!</h1>
    <p>Thanks for Using Liara.</p>
    <a class="btn" href="#">return</a>
</body>
</html>
"""

def send_email(request):
    subject = 'Django'
    message = 'Hello From Django.'
    from_email = 'main@example.com'
    recipient_list = ['example@example.com']

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    
    return HttpResponse(success_html)

