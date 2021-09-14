from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
#Have the root route render the main wireframe 
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses.html', context)

#Create the POST method to add new courses to the database
def create(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            course = Course.objects.create(
                course_name=request.POST['course_name'],
                description=request.POST['description'],
            )
            # description = Description.objects.create(content=request.POST['description'])
            # course.description = description
            # course.save()
            messages.success(request, "Course successfully created")
    return redirect('/') 
    
#function that renders the delete html page
def delete(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
        }
    return render(request,'delete.html', context)

def show_comment(request,course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request,'comments.html', context)

def create_comment(request, course_id):
    errors = Comment.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        # return redirect('/')
    else:
        Comment.objects.create(
            content=request.POST['content'],
            course = Course.objects.get(id=course_id)
        )
    return redirect('/courses/course_id/show_comment')

#I added line 59-61 and remove the place marker "pass"
def course_profile(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
    return render(request, 'comments.html')

    

#function of the delete function
def delete_page(request, course_id):    
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        course.delete()
    return redirect('/')

def delete_comment(request, comment_id):    
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect("/courses/{{course.id}}/show_comment")
