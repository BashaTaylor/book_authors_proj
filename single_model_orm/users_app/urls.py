from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),#Get request
    path('user/create', views.create_user),#POST
]