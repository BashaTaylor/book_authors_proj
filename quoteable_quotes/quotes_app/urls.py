from django.urls import path
from . import views #dot means: from the current file directory, import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),#registration
    path('login', views.login),#login
    path('success', views.success),#success page
    path('logout', views.logout),#log out
    # path('home', views.home),#Home/quotes page
    path('home', views.home),
    # path('books/add', views.add_book),#POST request for creating a new book (verb/redirecting),#function to add bk,top rt

    # path('books/<int:book_id>/favorite', views.favorite),#path to add favorite

    # path('books/<int:book_id>/unfavorite', views.unfavorite),#path to remove favorite from favorites

    # path('books/<int:book_id>', views.book),#path to go to Update.html page, bottom left page where you can update/delete book

    # path('books/<int:book_id>/update', views.update),#path to update the book

    # path('books/<int:book_id>/edit', views.edit),#edit book by id

    # path('books/<int:book_id>/delete', views.delete),
    
]