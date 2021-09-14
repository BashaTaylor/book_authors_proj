from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs.")
    # http://localhost:8000
def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog.")
    # http://localhost:8000/new
def create(request):
    return redirect('/')
    # http://localhost:8000/create
def show(request,number):
    return HttpResponse(f"Placeholder to display blog number: {number}")
    # http://localhost:8000/2021
def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")
    # http://localhost:8000/2021/edit
def destroy(request, number):
    return redirect('/')
    # http://localhost:8000/2021/delete