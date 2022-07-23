from accounts.views import LogoutView, RegisterView
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

accounts_urls = [
    path('register/', RegisterView, name="register"),
    path('logout/', LogoutView, name='logout'),
]
