from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import CommentForm
from .models import Post

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail

from .forms import CustomUserCreationForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # استفاده از فرم سفارشی
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            subject = 'welcome to Liara'
            message = "Thanks for Joining us in Liara"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [form.cleaned_data.get('email')]

            send_mail(subject, message, from_email, recipient_list)
            return redirect('home')
    else:
        form = CustomUserCreationForm()  # استفاده از فرم سفارشی
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # به جای 'home' به URL مورد نظر برای هدایت کاربر بعد از ورود بروید
        else:
            # اگر اطلاعات ورود نامعتبر باشد
            return render(request, 'login.html', {'error_message': 'نام کاربری یا رمز عبور اشتباه است'})
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def privacy_policy(request):
    return render(request, 'policy.html')

def contact_us(request):
    return render(request, 'contact.html')

from django.core.mail import send_mail
from django.conf import settings

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f'پیام از {name}'
        body = f'نام: {name}\nایمیل: {email}\nپیام: {message}'
        sender_email = settings.DEFAULT_FROM_EMAIL
        if form.is_valid():
            form.save()
            form = CustomUserCreationForm(request.POST) 
            recipient_list = [form.cleaned_data.get('email')]
        else:
            recipient_list = ['']

        send_mail(subject, body, sender_email, recipient_list)

    return render(request, 'contact.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home') 

