from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.

def index(request):
    context = {
        "time": strftime("%m-%d-%Y %H:%M %p %Z", gmtime())
    }
    return render(request, "index.html", context)
