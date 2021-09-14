from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),#Main page view
    path('courses/create', views.create), #Function to create a course
    path('courses/<int:course_id>/course_profile', views.course_profile),#Course profile view
    path('courses/<int:course_id>/show_comment', views.show_comment), #function to create a comment

    path('courses/<int:course_id>/create_comment', views.create_comment), 
    path('courses/<int:course_id>/delete_comment', views.delete_comment),   
    path('courses/<int:course_id>/delete', views.delete),#Function to delete a course on the confirmation page
    path('courses/<int:course_id>/delete_page', views.delete_page)#Delete profile view
]