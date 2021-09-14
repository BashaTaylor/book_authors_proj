from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, User
import bcrypt


# Create your views here.
def log_and_reg(request):
    return render(request, 'log_and_reg.html')
    
def register(request):
    errors = User.objects.register_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
    else:
        password = request.POST['password']
        hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hash_pw
        )
        request.session['userid'] = user.id
        messages.success(request, "Successfully registered account")
        return redirect('/')

    return redirect('/')

def login(request):
    users = User.objects.filter(email = request.POST['email'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST ['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            messages.success(request, "Successfully logged in")
            return redirect('/books')
        else:
            messages.error(request, "Invalid Email/Password Combo")
    else:
        messages.error(request, 'Account not found with email')
    return redirect('/')

def index(request):
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'all_books': Book.objects.all(),
        # 'book': 
    }
    return render(request, "index.html", context)

def show_one(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "books/books.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')

def books(request, book_id):
    #GET request to view one book at a time
    #Create a variable to get the book by id
    context = {
        'all_books': Book.objects.all(),
        'user': User.objects.get(id=request.session['userid']),
        'specific_book': Book.objects.get(id=book_id)

    }
    return render(request, "books.html", context)

def add_book(request):
    #POST request to add a book
    errors = Book.objects.book_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/books')
    else:
        my_user = User.objects.get(id=request.session['userid'])
        new_book = Book.objects.create(
            title = request.POST['title'], 
            description = request.POST['description'],
            uploaded_by = my_user
        )
        #this is creating many to many relationships:
        my_user.liked_books.add(new_book)
    return redirect('/books')

    #the name of the method is favorite:
def favorite(request, book_id):#POST
    book = Book.objects.get(id=book_id)
    my_user = User.objects.get(id=request.session['userid'])
    book.users_who_like.add(my_user)#many to many relationsships
    return redirect('/books')

def unfavorite(request, book_id):#POST
    book = Book.objects.get(id=book_id)
    my_user = User.objects.get(id=request.session['userid'])
    my_user.liked_books.remove(book)#many to many relationsships
    return redirect(f'/books/{book.id}')

def book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'my_user': User.objects.get(id=request.session['userid'])
    }
    return render(request, "update.html", context)

def update(request, book_id):
    errors = Book.objects.book_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
        # return redirect('/index')
    else:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.save()
        
    return redirect(f'/books/{book_id}')

def edit(request, book_id):
    errors = Book.objects.book_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
        # return redirect('/index')
    else:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.save()
        
    return redirect(f'/books/{book_id}')

def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()    
    return redirect('/books')




    # path('login', views.login),
    # path('index', views.index),
    # path('logout', views.logout),