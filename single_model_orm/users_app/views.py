from django.shortcuts import render, redirect
from.models import User

# Create your views here.
def index(request):
    context = {
        'all_users': User.objects.all(),
    }
    return render(request, 'home_page.html', context)

# CRUD
# GET=render
# POST= redirect


# Create
def create_user(request):
    #1 create the user
    new_user=User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], age=request.POST['age'])
    return redirect('/')
    # return render(request, 'home_page.html')