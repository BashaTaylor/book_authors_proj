from django.urls import path
from .import views

urlpatterns = [
    path('', views.index), #GET request redirecting
    path('users/create', views.create_user),#make a create_user method now in views.py
    path('dashboard', views.dashboard), #GETrequest to go to the dashboard page
    path('users/login', views.login), #make a login method in views.py
    path('logout', views.logout),
    path('create_trip', views.create_trip),#create a new trip function
    path('new', views.new), #Go to create a new trip page
    path('dashboard/<int:trip_id>/cancel_trip', views.cancel_trip),
    path('dashboard/<int:trip_id>/join', views.join),

    path('dashboard/<int:trip_id>/view', views.view),#Go to view page
    path('dashboard/<int:trip_id>/edit', views.edit),#Go to edit page
    path('dashboard/<int:trip_id>/delete',views.delete),# delete function
    path('dashboard/<int:trip_id>/update', views.update),#function to edit a job
]