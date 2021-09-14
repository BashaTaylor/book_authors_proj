from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('home', views.home),
    path('create', views.create),
    path('home/<int:quote_id>/edit', views.edit),
    path('home/<int:quote_id>/delete', views.delete),
    path('home/<int:quote_id>/update', views.update),
    path('users/<int:user_id>', views.summarize),
    path('home/<int:quote_id>/favorite', views.favorite),#path to add favorite
]