from django.urls import include, path

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("signup/", views.signup, name="signup"),  
    path("login/", views.login_view, name="login"),  
    path("about/", views.about, name="about"),  
    path("policy/", views.privacy_policy, name="privacy_policy"),
    path("contact/", views.contact_us, name='contact_us'),
    path("logout/", views.logout_view, name="logout"),
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]

