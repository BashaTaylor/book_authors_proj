from django.urls import path
from .import views
    
urlpatterns = [
    #localhost:800/new
    path('', views.index)
]