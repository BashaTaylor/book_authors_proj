from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    # context = {
    #     # 'users': User.objects.all()
    # }
    return render(request, 'log_reg.html')

    #change the 'all_shows" and Show.ob....
    # now we'll create a method
def create_user(request):
    if request.method == 'POST':
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            #this is the mambo-jumbo instead of actual password
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            # now create a user in your dataBase
            user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash) #make sure to make this pw_hash
            request.session['user_id'] = user.id
            return redirect('/main_page')
    return redirect('/')
# lets make a method called main page
def main_page(request):
    return render(request, 'main_page.html')

def login(request):
    if request.method == 'POST':
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/main_page')
        messages.error(request, 'Email or password are not correct')
    return redirect('/') 
    
