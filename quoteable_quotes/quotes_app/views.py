
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager 
import bcrypt

#Create your views here
def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
    else:
        password = request.POST['password']
        hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            email=request.POST['email'],
            password=hash_pw
        )
        request.session['userid'] = user.id
        messages.success(request, "Successfully registered account")
        return redirect('/success')

def login(request):
    print(request.POST)
    # retrieving a user from the db
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['password']:
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/home')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'my_user': User.objects.all()
    }
    return render(request, 'success.html', context)

def home(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'my_user': User.objects.all()
    }
    return render(request, 'home.html', context)
