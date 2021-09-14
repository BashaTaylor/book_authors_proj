from django.urls import path
from .import views

urlpatterns = [
    path('', views.index), #GET request redirecting to shows route
    path('shows', views.shows), #GET request to display all objects' info starting at a different root
    path('shows/new', views.new), #GET request to display form to create an object
    path('shows/create', views.create), #POST request to create an object

    path('shows/<int:show_id>/show', views.show), #GET request to display a specific object's info
    path('shows/<int:show_id>/edit', views.edit), #GET request to display form to update a specific object
    path('shows/<int:show_id>/update', views.update), #POST request to update a specific object
    path('shows/<int:show_id>/delete', views.delete), #POST request to delete a specific object
]
