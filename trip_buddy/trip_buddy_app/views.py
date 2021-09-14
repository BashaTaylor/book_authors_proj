from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    request.session.flush()
    context = {
        'all_trips': Trip.objects.all()
    }
    return render(request, 'index.html', context)

# Create a user
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
            return redirect('/dashboard')
    return redirect('/')
#Login
def login(request):
    if request.method == 'POST':
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/dashboard')
        messages.error(request, 'Email or password are not correct')
    return redirect('/') 

#making a method called dashboard
def dashboard(request):
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        'this_user': current_user,
        'all_trips' : Trip.objects.all().order_by('-created_at')
        # 'my_favorites' : current_user.favorite_quotes.all()
    }
    return render(request, 'dashboard.html', context)

#logout
def logout(request):
    request.session.flush()
    return redirect('/')

# #Go to the create new job page
def new(request):
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        'this_user': current_user,
        'all_trips' : Trip.objects.all(),
        # 'my_favorites' : current_user.favorite_quotes.all()
    }
    return render(request, 'new.html', context)

# #Create a new job 
def create_trip(request):
    if request.method != 'POST' or 'user_id' not in request.session:
        return redirect('')
    errors = Trip.objects.trip_validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    #we need to create a new job in database
    Trip.objects.create(
        destination = request.POST['destination'],
        start_date = request.POST['start_date'],
        end_date = request.POST['end_date'],
        plan = request.POST['plan'],
        created_by = User.objects.get(id=request.session['user_id'])
    )
    return redirect('/dashboard')

def cancel_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    user = User.objects.get(id=request.session['user_id'])
    trip.user_joined.remove(user)
    return redirect('/dashboard')



def join(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    user = User.objects.get(id=request.session['user_id'])
    trip.user_joined.add(user)
    return redirect('/dashboard')




def view(request, trip_id):
    one_trip = Trip.objects.get(id=trip_id)
    context = {
        'trip': one_trip,
        'this_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'trip.html', context)


# def edit(request, trip_id):
#     edit_trip = Trip.objects.get(id=trip_id)
#     edit_trip.destination = request.POST['destination']
#     edit_trip.start_date = request.POST['start_date']
#     edit_trip.end_date = request.POST['end_date']
#     edit_trip.plan = request.POST['plan']
#     errors = Trip.objects.trip_validator(request.POST)
#     print(errors)
#     if len(errors)>0:
#         for key, value in errors.items():
#             messages.error(request, value)
        
#         context = {
#             'trip': edit_trip,
#             'this_user': User.objects.get(id=request.session['user_id'])
#         }
#         return render(request, 'edit.html', context)    


def delete(request, trip_id):
    if request.method == 'POST':
        trip_to_delete = Trip.objects.get(id=trip_id)
        trip_to_delete.delete()
    return redirect('/dashboard')

def edit(request, trip_id):
    if request.method == 'GET':
        one_trip = Trip.objects.get(id=trip_id) 
        context = {
            'trip': one_trip,
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'edit.html', context)    

def update(request, trip_id):
    update_trip = Trip.objects.get(id=trip_id)
    update_trip.destination = request.POST['destination']
    update_trip.start_date = request.POST['start_date']
    update_trip.end_date = request.POST['end_date']
    update_trip.plan = request.POST['plan']
    errors = Trip.objects.trip_validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        context = {
            'trip': update_trip,
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'edit.html', context)
    update_trip.save()
    return redirect('/dashboard')

