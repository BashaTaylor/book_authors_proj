from django.shortcuts import render, redirect
from .models import Quote, User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'my_user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'success.html', context)
## Logging in and registering

def register(request):
    # if request.method != 'POST' or 'id' not in request.session:
    #     return redirect('')
    print(request.POST)
    # Create a user object
    errors = User.objects.basic_validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['pw']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        # now create a user in your dataBase
        new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['pw'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
    return redirect('/success')

def login(request):
    # if request.method != 'POST' or 'id' not in request.session:
    #     return redirect('')
    print(request.POST)
    # retrieving a user from the db
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        # if logged_user.password == request.POST['pw']:
        if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
            # request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
        return redirect('/home')
    else:
        messages.error(request, 'Account not found. Please use other email')
    
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def home(request): 
    # if 'id' not in request.session:
    #     return redirect('/')
    current_user = User.objects.get(id=request.session['id'])
    context = {
        'my_user': current_user,
        'all_quotes' : Quote.objects.all(),
        'my_favorites' : current_user.favorite_quotes.all()
    }
    return render(request, 'home.html', context)

def favorite(request, quote_id):#POST
    if request.method != 'POST' or 'id' not in request.session:
        return redirect('')
    quote = Quote.objects.get(id=quote_id)
    my_user = User.objects.get(id=request.session['id'])
    quote.user_likes.add(my_user)#many to many relationsships
    return redirect('/home')


def create(request): #POST
    if request.method != 'POST' or 'id' not in request.session:
        return redirect('')
    errors = Quote.objects.quote_validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home')
    #we need to create a new quote in database
    Quote.objects.create(
        message = request.POST['message'],
        quoted_by =  request.POST['quoted_by'],
        posted_by = User.objects.get(id=request.session['id'])
    )
    return redirect('/home')

def delete(request, quote_id): #POST - will redirect
    if request.method != 'POST' or 'id' not in request.session:
        return redirect('')
    deleting_quote = Quote.objects.get(id=quote_id)
    deleting_quote.delete()
    return redirect('/home')

def edit(request, quote_id): #GET request - it will render
    if 'id' not in request.session:
        return redirect('/')
    
    context = {
        'this_user': User.objects.get(id=request.session['id']),
        'this_quote': Quote.objects.get(id=quote_id), 
    }
    return render(request, 'edit.html', context)

def update(request,quote_id): #POST request
    if request.method != 'POST' or 'id' not in request.session:
        return redirect('')
    errors = Quote.objects.quote_validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        context = {
        'this_user': User.objects.get(id=request.session['id']),
        'this_quote': Quote.objects.get(id=quote_id), 
    }
        return render(request, 'edit.html', context)
    updating_quote = Quote.objects.get(id=quote_id)
    updating_quote.message = request.POST['message']
    updating_quote.quoted_by = request.POST['quoted_by']
    updating_quote.save()
    return redirect('/home')

def summarize(request, user_id): #GET
    if 'id' not in request.session:
        return redirect('/')
        
    current_user = User.objects.get(id=user_id)
    print(current_user.first_name)
    all_quotes = Quote.objects.all()
    count = 0
    for quote in all_quotes:
        if quote.posted_by.id == current_user.id:
            count += 1
    context = {
        'count': count,
        # 'this_user' : User.objects.get(id=user_id),
        'this_user': current_user,
        # 'all_quotes': Quote.objects.all(),
        'all_quotes': all_quotes,
    }
    return render(request, 'summary.html', context)