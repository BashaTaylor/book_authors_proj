from django.urls import path
from .import views

urlpatterns = [
    path('', views.index), #GET request redirecting to shows route
    path('users/create', views.create_user),#make a create_user method now in views.py
    path('main_page', views.main_page),#make main_page def method in views
    path('users/login', views.login) #now make a login method in views.py
]