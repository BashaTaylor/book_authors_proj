"""favorite_books_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views #dot means: from the current file directory, import views

urlpatterns = [
    path('', views.log_and_reg),
    path('register', views.register),#registration
    path('login', views.login),#login
    path('books', views.index),#main/welcome page
    path('logout', views.logout),#log out
    
    path('books/add', views.add_book),#POST request for creating a new book (verb/redirecting),#function to add bk,top rt

    path('books/<int:book_id>/favorite', views.favorite),#path to add favorite

    path('books/<int:book_id>/unfavorite', views.unfavorite),#path to remove favorite from favorites

    path('books/<int:book_id>', views.book),#path to go to Update.html page, bottom left page where you can update/delete book

    path('books/<int:book_id>/update', views.update),#path to update the book

    path('books/<int:book_id>/edit', views.edit),#edit book by id

    path('books/<int:book_id>/delete', views.delete),
    
]