from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def new(request):
    return render(request, 'add_new_show.html')
    #new is good

#Create
def create(request):
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect('/')

#Read
def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'tv_show.html', context)


def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'edit_show.html', context)
    
#Update
def update(request, show_id):
    # update show!
    to_update = Show.objects.get(id=show_id)
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect('/')


def delete(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/')
