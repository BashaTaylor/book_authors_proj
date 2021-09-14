from django.urls import path     
from . import views
urlpatterns = [
    # same thing as localhoast:8000 (if I type localhost:800 in my url, it is the same as the path '' with nothing inside of it)
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>', views.show),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
] 